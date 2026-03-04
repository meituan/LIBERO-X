"""
Multi-level Testset Builder
---------------------------
Reusable factory to derive test scenes from training scenes by expanding
object placement regions (region ranges) with randomized scaling and
collision/boundary checks.
"""
from __future__ import annotations

import re
from typing import Dict, Tuple, Callable, Optional, Iterable, Type, List

from libero.libero.utils.mu_utils import InitialSceneTemplates, register_mu
from libero.libero.utils.bddl_generation_utils import (
    get_xy_region_kwargs_list_from_regions_info,
)

# Types
WorkspaceBoundsFn = Callable[[Optional[str]], Tuple[float, float, float, float]]
ObjectRadiusFn = Callable[[str], float]


def _noop_workspace_bounds(_: Optional[str]) -> Tuple[float, float, float, float]:
    return (-1e9, 1e9, -1e9, 1e9)


def default_workspace_bounds(_: Optional[str]) -> Tuple[float, float, float, float]:
    return (-0.4, 0.4, -0.4, 0.4)



def _dist2(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    dx = p[0] - q[0]
    dy = p[1] - q[1]
    return dx * dx + dy * dy

def _dist(p: Tuple[float, float], q: Tuple[float, float]) -> float:
    return (_dist2(p, q)) ** 0.5


def _ranges_to_center_half_len(rng: Tuple[float, float, float, float]) -> Tuple[Tuple[float, float], float]:
    xmin, ymin, xmax, ymax = rng
    cx = (xmin + xmax) * 0.5
    cy = (ymin + ymax) * 0.5
    hlx = (xmax - xmin) * 0.5
    hly = (ymax - ymin) * 0.5
    return (cx, cy), max(hlx, hly)


def _center_half_len_to_ranges(center: Tuple[float, float], half_len: float) -> Tuple[float, float, float, float]:
    cx, cy = center
    return (cx - half_len, cy - half_len, cx + half_len, cy + half_len)


def _collect_half_lens(regions: Dict[str, Dict]) -> Dict[str, float]:
    """Collect the current half-length of each region (inferred from ranges)."""
    result: Dict[str, float] = {}
    for k, info in regions.items():
        rngs = info.get("ranges")
        if not rngs:
            continue
        center, hl = _ranges_to_center_half_len(tuple(rngs[0]))  # type: ignore
        result[k] = float(hl)
    return result


def _get_center_and_hl_of_region(regions: Dict[str, Dict], name: str) -> Optional[Tuple[Tuple[float, float], float]]:
    info = regions.get(name)
    if not info:
        return None
    rngs = info.get("ranges")
    if not rngs:
        return None
    center, hl = _ranges_to_center_half_len(tuple(rngs[0]))  # type: ignore
    return (center, float(hl))


def _set_region_center_preserve_hl(regions: Dict[str, Dict], name: str, center: Tuple[float, float]) -> None:
    res = _get_center_and_hl_of_region(regions, name)
    if res is None:
        return
    _, hl = res
    regions[name]["ranges"] = [_center_half_len_to_ranges(center, hl)]


def _collect_centers(regions: Dict[str, Dict]) -> Dict[str, Tuple[float, float]]:
    out: Dict[str, Tuple[float, float]] = {}
    for k in regions.keys():
        res = _get_center_and_hl_of_region(regions, k)
        if res is None:
            continue
        c, _ = res
        out[k] = (float(c[0]), float(c[1]))
    return out


def _apply_scaling_pairwise_half_distance(
    regions: Dict[str, Dict],
    *,
    margin: float = 0.0,
    per_object_margin: Optional[Dict[str, float]] = None,
    debug_print: bool = True,
) -> None:
    """Simplest strategy: for each region i, compute center distance d(i,j)
    to all other regions j, then use half of the minimum value, min_j d(i,j)/2,
    as the new half_len and update ranges."""
    keys = list(regions.keys())
    ordered_keys: List[str] = []
    centers: List[Tuple[float, float]] = []

    for k in keys:
        info = regions[k]
        rngs = info.get("ranges")
        if not rngs:
            continue
        center, _ = _ranges_to_center_half_len(tuple(rngs[0]))  # type: ignore
        ordered_keys.append(k)
        centers.append(center)

    n = len(ordered_keys)
    for i, name in enumerate(ordered_keys):
        if n <= 1:
            continue
        min_half = float("inf")
        for j in range(n):
            if i == j:
                continue
            d = _dist(centers[i], centers[j])
            half = 0.5 * d
            if half < min_half:
                min_half = half
        # Compute the effective margin for this object (allow per-name substring override)
        eff_margin = margin
        if per_object_margin:
            for key, m in per_object_margin.items():
                if key in name:
                    # If multiple keys match, use the larger margin (more conservative)
                    eff_margin = max(eff_margin, float(m))
        new_hl = float(max(0.01, min_half - eff_margin))
        regions[name]["ranges"] = [
            _center_half_len_to_ranges(centers[i], new_hl)
        ]
        if debug_print:
            cx, cy = centers[i]
            print(f"[Level2-PairSimple] {name}: center=({cx:.3f},{cy:.3f}), min_half={min_half:.4f}, margin={eff_margin:.4f}, new_hl={new_hl:.4f}")

def make_expanded_region_scene_level2(
    training_scene_cls: Type[InitialSceneTemplates],
    *,
    new_class_name: Optional[str] = None,
    scene_type: str = "kitchen",
    margin: float = 0.0,
    per_object_margin: Optional[Dict[str, float]] = None,
):
    """Level-2 builder: derive a test-scene subclass by expanding region ranges.

    Level-2 goal: reuse training scenes, enlarge random placement regions while
    preserving relative layout and avoiding collisions.
    """
    base_name = training_scene_cls.__name__
    new_name = new_class_name or (base_name + "_TestExpanded")

    # define the override in a closure so it can call the parent define_regions
    def _define_regions(self):  # type: ignore
        # call parent define_regions
        training_scene_cls.define_regions(self)
        # Apply collision-aware expansion and print change details
        print(f"[Level2] scene '{self.__class__.__name__}' workspace='{getattr(self, 'workspace_name', None)}'")
        before = _collect_half_lens(self.regions)
        # Use the simple "half of center distance" expansion strategy
        # (ignores boundaries, object radii, and upper/lower limits)
        _apply_scaling_pairwise_half_distance(
            self.regions,
            margin=margin,
            per_object_margin=per_object_margin,
            debug_print=True,
        )
        after = _collect_half_lens(self.regions)
        for k, old_hl in before.items():
            new_hl = after.get(k, old_hl)
            if abs(new_hl - old_hl) > 1e-9:
                print(f"[Level2] region '{k}': half_len {old_hl:.4f} -> {new_hl:.4f}")
        # refresh regions list used by generators
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    # create a new class with the intended name, then register it so MU key matches
    Derived = type(new_name, (training_scene_cls,), {"define_regions": _define_regions})  # type: ignore
    Derived = register_mu(scene_type=scene_type)(Derived)
    return Derived


# Backward-compatible alias (kept for older code paths). Prefer the explicit level-2 name.
make_expanded_region_scene = make_expanded_region_scene_level2


def make_expanded_region_scene_level3(
    training_scene_cls: Type[InitialSceneTemplates],
    *,
    new_class_name: Optional[str] = None,
    scene_type: str = "kitchen",
    # Objects that never participate in swapping: if region name contains any
    # of these substrings, treat it as a fixed large object.
    fixed_region_prefixes: Iterable[str] = (),
    # Name keywords for medium objects (region name contains any => medium)
    mid_region_keywords: Iterable[str] = ("stove", "drainer"),
    # Name keywords for small objects (region name contains any => small)
    small_region_keywords: Iterable[str] = ("bowl", "mug", "book", "plate", "bottle", "pot"),
    # objects_of_interest: object names to prioritize for relocation
    relocate_object_names: Optional[Iterable[str]] = None,
    rng_seed: Optional[int] = None,
    # Level-2 preprocessing (run one simple half-distance expansion first)
    do_level2_first: bool = True,
    level2_margin: float = 0.0,
    level2_per_object_margin: Optional[Dict[str, float]] = None,
):
   

    base_name = training_scene_cls.__name__
    new_name = new_class_name or (base_name + "Level3")

    def _define_regions(self):  # type: ignore
        # 1) Base regions
        training_scene_cls.define_regions(self)
        print(f"[Level3] scene '{self.__class__.__name__}' workspace='{getattr(self, 'workspace_name', None)}'")
        # 2) Optional: run Level-2 simple half-distance expansion first
        # (changes only half_len, not center positions)
        if do_level2_first:
            print("[Level3] pre-level2: pairwise half-distance expand")
            _apply_scaling_pairwise_half_distance(
                self.regions,
                margin=level2_margin,
                per_object_margin=level2_per_object_margin,
                debug_print=True,
            )

        # 3) Level-3: center-swapping strategy based on large/medium/small categories
        #    Debug: record centers before swapping
        pre_centers = _collect_centers(self.regions)
        # 3.0 Prepare keyword lists and define the size classification function
        fixed_keys = list(fixed_region_prefixes)
        mid_keys = list(mid_region_keywords)
        small_keys = list(small_region_keywords)

        def _classify_region_size(name: str) -> str:
            """
            Classify a region by keywords in its name:
            - 'fixed': never participates in swapping
            - 'mid': medium object
            - 'small': small object
            If no keyword matches, default to 'fixed' (not swappable).
            """
            for key in fixed_keys:
                if key and key in name:
                    return "fixed"
            for key in mid_keys:
                if key and key in name:
                    return "mid"
            for key in small_keys:
                if key and key in name:
                    return "small"
            return "fixed"

        # 3.1 Classify all regions in the scene into fixed/mid/small
        region_size: Dict[str, str] = {}
        all_mid_regions: List[str] = []
        all_small_regions: List[str] = []
        for rname in self.regions.keys():
            size = _classify_region_size(rname)
            region_size[rname] = size
            if size == "mid":
                all_mid_regions.append(rname)
            elif size == "small":
                all_small_regions.append(rname)

        # 3.2 Use init_states and objects_of_interest to map target objects to regions,
        #     then classify them by fixed/mid/small (fixed ones never swap)
        target_mid_regions: List[str] = []
        target_small_regions: List[str] = []
        if relocate_object_names is not None:
            target_objs = set(relocate_object_names)
            ws = getattr(self, "workspace_name", None)
            try:
                for st in getattr(self, "init_states", []):
                    if not isinstance(st, (list, tuple)) or len(st) < 3:
                        continue
                    obj = st[1]
                    reg_full = st[2]
                    if obj not in target_objs or not isinstance(reg_full, str):
                        continue
                    # 1) Direct match
                    candidates: List[str] = []
                    if reg_full in self.regions:
                        candidates.append(reg_full)
                    # 2) Match after stripping workspace prefix
                    #    (e.g., "kitchen_table_" + name)
                    if ws and reg_full.startswith(ws + "_"):
                        reg_stripped = reg_full[len(ws) + 1 :]
                        if reg_stripped in self.regions:
                            candidates.append(reg_stripped)
                    # 3) Generic prefix stripping: if it contains "_", remove first segment
                    if "_" in reg_full:
                        parts = reg_full.split("_", 1)
                        reg_tail = parts[1]
                        if reg_tail in self.regions:
                            candidates.append(reg_tail)
                    # Classify based on the resolved region name
                    for rname in candidates:
                        size = region_size.get(rname, "fixed")
                        if size == "mid":
                            if rname not in target_mid_regions:
                                target_mid_regions.append(rname)
                        elif size == "small":
                            if rname not in target_small_regions:
                                target_small_regions.append(rname)
                        else:
                            print(f"[Level3] skip target region '{rname}' (fixed/large)")
            except Exception:
                target_mid_regions = []
                target_small_regions = []

        import random
        if rng_seed is not None:
            random.seed(rng_seed)

        # 3.3 Swap among medium objects:
        #     - Targets: regions for medium objects in objects_of_interest
        #     - Candidates: all medium-object regions in the scene
        #       (including or excluding other objects_of_interest)
        used_regions = set()
        for t in list(target_mid_regions):
            if t in used_regions:
                continue
            cand_list = [r for r in all_mid_regions if r not in used_regions and r != t]
            if not cand_list:
                print(f"[Level3] mid swap '{t}': no candidate, skip")
                continue
            c = random.choice(cand_list)
            used_regions.add(t)
            used_regions.add(c)
            t_data = _get_center_and_hl_of_region(self.regions, t)
            c_data = _get_center_and_hl_of_region(self.regions, c)
            if t_data is None or c_data is None:
                print(f"[Level3] mid swap '{t}' <-> '{c}': missing data, skip")
                continue
            (tc, _), (cc, _) = t_data, c_data
            _set_region_center_preserve_hl(self.regions, t, cc)
            _set_region_center_preserve_hl(self.regions, c, tc)
            print(f"[Level3] mid swap centers: '{t}' <-> '{c}'")

        # 3.4 Swap among small objects:
        #     - Targets: regions for small objects in objects_of_interest
        #     - Candidates: all small-object regions in the scene
        for t in list(target_small_regions):
            if t in used_regions:
                continue
            cand_list = [r for r in all_small_regions if r not in used_regions and r != t]
            if not cand_list:
                print(f"[Level3] small swap '{t}': no candidate, skip")
                continue
            c = random.choice(cand_list)
            used_regions.add(t)
            used_regions.add(c)
            t_data = _get_center_and_hl_of_region(self.regions, t)
            c_data = _get_center_and_hl_of_region(self.regions, c)
            if t_data is None or c_data is None:
                print(f"[Level3] small swap '{t}' <-> '{c}': missing data, skip")
                continue
            (tc, _), (cc, _) = t_data, c_data
            _set_region_center_preserve_hl(self.regions, t, cc)
            _set_region_center_preserve_hl(self.regions, c, tc)
            print(f"[Level3] small swap centers: '{t}' <-> '{c}'")

        # Debug: print center changes before and after swaps
        post_centers = _collect_centers(self.regions)
        print("[Level3] centers before -> after:")
        try:
            for k in sorted(post_centers.keys()):
                pc = pre_centers.get(k)
                qc = post_centers.get(k)
                if pc is None or qc is None:
                    continue
                print(f"[Level3]  - {k}: ({pc[0]:.3f},{pc[1]:.3f}) -> ({qc[0]:.3f},{qc[1]:.3f})")
        except Exception:
            pass
        # 4) Refresh region list
        self.xy_region_kwargs_list = get_xy_region_kwargs_list_from_regions_info(self.regions)

    Derived = type(new_name, (training_scene_cls,), {"define_regions": _define_regions})  # type: ignore
    Derived = register_mu(scene_type=scene_type)(Derived)
    return Derived
