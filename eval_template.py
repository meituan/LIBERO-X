import collections
import dataclasses
import hashlib
import json
import logging
import math
import os
import pathlib
import re

import imageio
import numpy as np
import torch
import tqdm
import tyro
from typing import Optional
from natsort import natsorted
from libero.libero.envs import OffScreenRenderEnv
from libero.libero.utils.parse_bddl import parse_bddl_file
from openpi_client import image_tools
from openpi_client import websocket_client_policy as _websocket_client_policy

LIBERO_DUMMY_ACTION = [0.0] * 6 + [-1.0]
LIBERO_ENV_RESOLUTION = 256


def _make_task_segment(scene_name: str, task_id: int, task_description: str, max_len: int = 180) -> str:
    base = f"{scene_name}_{str(task_id).zfill(3)}_{task_description.replace(' ', '_')}"
    safe = re.sub(r"[^A-Za-z0-9_]+", "_", base)
    if len(safe) > max_len:
        hash_suffix = hashlib.md5(safe.encode("utf-8")).hexdigest()[:8]
        keep_len = max_len - len(hash_suffix) - 1
        keep_len = max(1, keep_len)
        safe = f"{safe[:keep_len].rstrip('_')}_{hash_suffix}"
    return safe


def _quat2axisangle(quat):
    if quat[3] > 1.0:
        quat[3] = 1.0
    elif quat[3] < -1.0:
        quat[3] = -1.0
    den = np.sqrt(1.0 - quat[3] * quat[3])
    if math.isclose(den, 0.0):
        return np.zeros(3)
    return (quat[:3] * 2.0 * math.acos(quat[3])) / den


def _parse_bddl_task_key(bddl_name: str) -> tuple[str, str]:
    m = re.search(r"__T(\d+)(?:__A(\d+))?", bddl_name)
    if not m:
        raise ValueError(f"Could not parse task id from BDDL name: {bddl_name}")
    task_id = m.group(1).zfill(3)
    variant = f"A{m.group(2)}" if m.group(2) else ""
    return task_id, variant


def _load_level5_prompts(prompt_root: pathlib.Path) -> dict[str, dict[tuple[str, str], str]]:
    prompt_files = sorted(prompt_root.glob("L5-*.jsonl"))
    if not prompt_files:
        raise FileNotFoundError(f"No L5-*.jsonl files found under {prompt_root}")
    prompt_map: dict[str, dict[tuple[str, str], str]] = {}
    for path in prompt_files:
        tag = path.stem
        per_tag: dict[tuple[str, str], str] = {}
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                task_id = str(rec.get("task_id", "")).zfill(3)
                variant = rec.get("variant") or ""
                task_desc = rec.get("task_desc", "")
                if not task_id or not task_desc:
                    continue
                per_tag[(task_id, variant)] = task_desc
        prompt_map[tag] = per_tag
    return prompt_map


@dataclasses.dataclass
class Args:
    # Remote model server
    host: str = "127.0.0.1"
    port: int = 8000
    resize_size: int = 224
    replan_steps: int = 25

    # Scene/data loading
    scene_group: str = "LEVEL1"  # LEVEL1-LEVEL5
    load_mode: str = "bddl"  # "bddl" or "init"
    bddl_root: str = "libero/libero_x/bddl"
    init_root: str = "libero/libero_x/init"
    level5_prompt_root: str = "libero/libero_x/LEVEL5"
    num_trials_per_task: int = 10
    num_steps_wait: int = 10
    max_steps: int = 1200
    flip_images: bool = False

    # Output
    video_out_path: str = "data/eval_videos"
    results_out_path: str = ""  # optional jsonl; defaults to video_out_path/scene
    save_all_videos: bool = True
    fps: int = 10

    seed: int = 7


def eval_template(args: Args) -> None:
    np.random.seed(args.seed)

    scene_group = args.scene_group.upper()
    if scene_group not in {"LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"}:
        raise ValueError(f"scene_group must be LEVEL1-LEVEL5, got: {args.scene_group}")
    base_level = "LEVEL4" if scene_group == "LEVEL5" else scene_group

    bddl_dir = pathlib.Path(args.bddl_root) / base_level
    bddl_files = natsorted([f for f in os.listdir(bddl_dir) if f.endswith(".bddl")])

    init_dir_root = None
    if args.load_mode.lower() == "init":
        init_dir_root = pathlib.Path(args.init_root) / base_level

    output_group = scene_group
    video_out_path = pathlib.Path(args.video_out_path) / output_group
    video_out_path.mkdir(parents=True, exist_ok=True)
    results_out_path = pathlib.Path(args.results_out_path) if args.results_out_path else (
        video_out_path / f"results_{output_group}.jsonl"
    )
    results_out_path.parent.mkdir(parents=True, exist_ok=True)

    prompt_map = None
    prompt_order = None
    if scene_group == "LEVEL5":
        if not args.level5_prompt_root:
            raise ValueError("LEVEL5 requires level5_prompt_root to be set.")
        prompt_map = _load_level5_prompts(pathlib.Path(args.level5_prompt_root))
        prompt_order = sorted(prompt_map.keys())

    client = _websocket_client_policy.WebsocketClientPolicy(args.host, args.port)

    total_episodes = 0
    total_successes = 0

    for task_id in tqdm.tqdm(range(len(bddl_files))):
        bddl_file_path = bddl_dir / bddl_files[task_id]
        scene_match = re.search(r"SCENE\d+", bddl_files[task_id])
        scene_name = scene_match.group() if scene_match else base_level
        task_description = parse_bddl_file(bddl_file_path)["language"]
        prompt_candidates = None
        if prompt_map is not None:
            key = _parse_bddl_task_key(bddl_file_path.name)
            prompt_candidates = []
            for tag in prompt_order:
                per_tag = prompt_map.get(tag, {})
                if key not in per_tag:
                    raise KeyError(f"Missing prompt for tag {tag}, key={key}, file={bddl_file_path.name}")
                prompt_candidates.append((tag, per_tag[key]))

        if init_dir_root is not None:
            bddl_name = bddl_file_path.stem
            init_path = init_dir_root / f"{bddl_name}.init"
            if not init_path.exists():
                raise FileNotFoundError(f"Init file not found: {init_path}")
            states_tensor = torch.load(init_path)
            episode_indices = range(len(states_tensor))
        else:
            states_tensor = None
            episode_indices = range(args.num_trials_per_task)

        task_episodes = 0
        task_successes = 0

        for ep_id in episode_indices:
            prompt_tag = ""
            if prompt_candidates is not None:
                prompt_idx = (ep_id // 2) % len(prompt_candidates)
                prompt_tag, task_description = prompt_candidates[prompt_idx]
            replay_images = []
            done = False

            try:
                env_args = {
                    "bddl_file_name": bddl_file_path,
                    "camera_heights": LIBERO_ENV_RESOLUTION,
                    "camera_widths": LIBERO_ENV_RESOLUTION,
                    "horizon": args.max_steps + args.num_steps_wait + 1,
                }
                env = OffScreenRenderEnv(**env_args)
                env.seed(ep_id)
                env.reset()

                if states_tensor is not None:
                    state_vec = states_tensor[ep_id]
                    obs = env.regenerate_obs_from_state(state_vec.numpy() if hasattr(state_vec, "numpy") else state_vec)
                    t = args.num_steps_wait
                else:
                    obs = None
                    t = 0
            except Exception as e:
                logging.error(f"Failed to initialize env for {bddl_file_path} ep {ep_id}: {e}")
                _write_result(
                    results_out_path,
                    args,
                    scene_name,
                    task_id,
                    bddl_file_path,
                    task_description,
                    ep_id,
                    False,
                    "",
                    prompt_tag=prompt_tag,
                    failure_stage="scene_init",
                    error=e,
                )
                total_episodes += 1
                task_episodes += 1
                continue

            action_plan = collections.deque()
            while t < args.max_steps + args.num_steps_wait:
                try:
                    if t < args.num_steps_wait:
                        obs, reward, done, info = env.step(LIBERO_DUMMY_ACTION)
                        t += 1
                        continue

                    if args.flip_images:
                        img = np.ascontiguousarray(obs["agentview_image"][::-1, ::-1])
                        wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, ::-1])
                    else:
                        img = np.ascontiguousarray(obs["agentview_image"][::-1, :])
                        wrist_img = np.ascontiguousarray(obs["robot0_eye_in_hand_image"][::-1, :])

                    img = image_tools.convert_to_uint8(
                        image_tools.resize_with_pad(img, args.resize_size, args.resize_size)
                    )
                    wrist_img = image_tools.convert_to_uint8(
                        image_tools.resize_with_pad(wrist_img, args.resize_size, args.resize_size)
                    )
                    replay_images.append(img)

                    if not action_plan:
                        element = {
                            "observation/image": img,
                            "observation/wrist_image": wrist_img,
                            "observation/state": np.concatenate(
                                (
                                    obs["robot0_eef_pos"],
                                    _quat2axisangle(obs["robot0_eef_quat"]),
                                    obs["robot0_gripper_qpos"],
                                )
                            ),
                            "prompt": str(task_description),
                        }
                        resp = client.infer(element)
                        action_chunk = resp["actions"]
                        if len(action_chunk) == 0:
                            raise RuntimeError("Policy returned zero actions.")
                        chunk_len = min(len(action_chunk), args.replan_steps)
                        action_plan.extend(action_chunk[:chunk_len])

                    action = action_plan.popleft()
                    obs, reward, done, info = env.step(action.tolist())
                    if done:
                        break
                    t += 1
                except Exception as e:
                    logging.error(f"Caught exception during rollout: {e}")
                    break

            total_episodes += 1
            task_episodes += 1
            if done:
                total_successes += 1
                task_successes += 1

            suffix = "success" if done else "failure"
            task_segment = _make_task_segment(scene_name, task_id, task_description)
            ep_tag = f"ep{str(ep_id + 1).zfill(3)}"
            video_path = video_out_path / f"rollout_{task_segment}_{ep_tag}_{suffix}.mp4"

            should_save_video = bool(replay_images) and args.save_all_videos
            if should_save_video:
                try:
                    imageio.mimwrite(video_path, [np.asarray(x) for x in replay_images], fps=args.fps)
                except OSError as e:
                    logging.error(f"Failed to write video {video_path}: {e}")

            _write_result(
                results_out_path,
                args,
                scene_name,
                task_id,
                bddl_file_path,
                task_description,
                ep_id,
                done,
                str(video_path),
                prompt_tag=prompt_tag,
            )

        logging.info(
            "Task %s: %d/%d (%.1f%%)",
            task_id,
            task_successes,
            task_episodes,
            (task_successes / task_episodes * 100.0) if task_episodes else 0.0,
        )

    success_rate = (total_successes / total_episodes) if total_episodes else 0.0
    logging.info("Total success rate: %.4f (%d/%d)", success_rate, total_successes, total_episodes)

    summary = {
        "scene_group": output_group,
        "total_episodes": total_episodes,
        "total_successes": total_successes,
        "success_rate": success_rate,
    }
    summary_path = video_out_path / "summary.json"
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)


def _write_result(
    results_out_path: pathlib.Path,
    args: Args,
    scene_name: str,
    task_id: int,
    bddl_file_path: pathlib.Path,
    task_description: str,
    ep_id: int,
    done: bool,
    video_path: str,
    prompt_tag: str = "",
    failure_stage: Optional[str] = None,
    error: Optional[Exception] = None,
) -> None:
    result = {
        "scene_group": str(args.scene_group.upper()),
        "scene_name": str(scene_name),
        "task_id": int(task_id),
        "task_file": str(bddl_file_path),
        "task_desc": str(task_description),
        "prompt_tag": str(prompt_tag),
        "episode_index": int(ep_id),
        "success": bool(done),
        "video_path": str(video_path),
    }
    if failure_stage:
        result["failure_stage"] = failure_stage
    if error is not None:
        result["error_type"] = type(error).__name__
        result["error_message"] = str(error)
    with open(results_out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    args = tyro.cli(Args)
    eval_template(args)
