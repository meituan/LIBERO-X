import abc
import os
import glob
import random
import torch

from typing import List, NamedTuple, Type
from libero.libero import get_libero_path
from libero.libero.benchmark.libero_suite_task_map import libero_task_map

BENCHMARK_MAPPING = {}


def register_benchmark(target_class):
    """We design the mapping to be case-INsensitive."""
    BENCHMARK_MAPPING[target_class.__name__.lower()] = target_class
    aliases = getattr(target_class, "ALIASES", [])
    for name in aliases:
        BENCHMARK_MAPPING[str(name).lower()] = target_class


def get_benchmark_dict(help=False):
    if help:
        print("Available benchmarks:")
        for benchmark_name in BENCHMARK_MAPPING.keys():
            print(f"\t{benchmark_name}")
    return BENCHMARK_MAPPING


def get_benchmark(benchmark_name):
    return BENCHMARK_MAPPING[benchmark_name.lower()]


def print_benchmark():
    print(BENCHMARK_MAPPING)


class Task(NamedTuple):
    name: str
    language: str
    problem: str
    problem_folder: str
    bddl_file: str
    init_states_file: str


def grab_language_from_filename(x):
    if x[0].isupper():  # LIBERO-100
        if "SCENE10" in x:
            language = " ".join(x[x.find("SCENE") + 8 :].split("_"))
        else:
            language = " ".join(x[x.find("SCENE") + 7 :].split("_"))
    else:
        language = " ".join(x.split("_"))
    en = language.find(".bddl")
    return language[:en]


libero_suites = [
    "libero_spatial",
    "libero_object",
    "libero_goal",
    "libero_90",
    "libero_10",
]
task_maps = {}
max_len = 0
for libero_suite in libero_suites:
    task_maps[libero_suite] = {}

    for task in libero_task_map[libero_suite]:
        language = grab_language_from_filename(task + ".bddl")
        task_maps[libero_suite][task] = Task(
            name=task,
            language=language,
            problem="Libero",
            problem_folder=libero_suite,
            bddl_file=f"{task}.bddl",
            init_states_file=f"{task}.pruned_init",
        )

        # print(language, "\n", f"{task}.bddl", "\n")
        # print("")


task_orders = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 6, 8, 7, 3, 1, 2, 0, 9, 5],
    [6, 3, 5, 0, 4, 2, 9, 1, 8, 7],
    [7, 4, 3, 0, 8, 1, 2, 5, 9, 6],
    [4, 5, 6, 3, 8, 0, 2, 7, 1, 9],
    [1, 2, 3, 0, 6, 9, 5, 7, 4, 8],
    [3, 7, 8, 1, 6, 2, 9, 4, 0, 5],
    [4, 2, 9, 7, 6, 8, 5, 1, 3, 0],
    [1, 8, 5, 4, 0, 9, 6, 7, 2, 3],
    [8, 3, 6, 4, 9, 5, 1, 2, 0, 7],
    [6, 9, 0, 5, 7, 1, 2, 8, 3, 4],
    [6, 8, 3, 1, 0, 2, 5, 9, 7, 4],
    [8, 0, 6, 9, 4, 1, 7, 3, 2, 5],
    [3, 8, 6, 4, 2, 5, 0, 7, 1, 9],
    [7, 1, 5, 6, 3, 2, 8, 9, 4, 0],
    [2, 0, 9, 5, 3, 6, 8, 7, 1, 4],
    [3, 5, 9, 6, 2, 4, 8, 7, 1, 0],
    [7, 6, 5, 9, 0, 3, 4, 2, 8, 1],
    [2, 5, 0, 9, 3, 1, 6, 4, 8, 7],
    [3, 5, 1, 2, 7, 8, 6, 0, 4, 9],
    [3, 4, 1, 9, 7, 6, 8, 2, 0, 5],
]


def _build_libero_x_tasks(level: int) -> List["Task"]:
    level_dir = f"SCENE_LEVEL{level}"
    bddl_root = os.environ.get("LIBERO_X_BDDL_ROOT", get_libero_path("bddl_files"))
    init_root = os.environ.get("LIBERO_X_INIT_ROOT", get_libero_path("init_states"))
    bddl_dir = os.path.join(bddl_root, level_dir)
    init_dir = os.path.join(init_root, level_dir)
    if not os.path.isdir(bddl_dir):
        raise FileNotFoundError(f"BDDL directory not found: {bddl_dir}")
    if not os.path.isdir(init_dir):
        raise FileNotFoundError(f"Init directory not found: {init_dir}")

    tasks: List[Task] = []
    for bddl_path in sorted(glob.glob(os.path.join(bddl_dir, "*.bddl"))):
        name = os.path.splitext(os.path.basename(bddl_path))[0]
        language = grab_language_from_filename(name + ".bddl")
        tasks.append(
            Task(
                name=name,
                language=language,
                problem="LiberoX",
                problem_folder=level_dir,
                bddl_file=f"{name}.bddl",
                init_states_file=f"{name}.init",
            )
        )
    return tasks


class Benchmark(abc.ABC):
    """A Benchmark."""

    def __init__(self, task_order_index=0):
        self.task_embs = None
        self.task_order_index = task_order_index

    def _make_benchmark(self):
        tasks = list(task_maps[self.name].values())
        if self.name == "libero_90":
            self.tasks = tasks
        else:
            print(f"[info] using task orders {task_orders[self.task_order_index]}")
            self.tasks = [tasks[i] for i in task_orders[self.task_order_index]]
        self.n_tasks = len(self.tasks)

    def get_num_tasks(self):
        return self.n_tasks

    def get_task_names(self):
        return [task.name for task in self.tasks]

    def get_task_problems(self):
        return [task.problem for task in self.tasks]

    def get_task_bddl_files(self):
        return [task.bddl_file for task in self.tasks]

    def get_task_bddl_file_path(self, i):
        bddl_file_path = os.path.join(
            get_libero_path("bddl_files"),
            self.tasks[i].problem_folder,
            self.tasks[i].bddl_file,
        )
        return bddl_file_path

    def get_task_demonstration(self, i):
        assert (
            0 <= i and i < self.n_tasks
        ), f"[error] task number {i} is outer of range {self.n_tasks}"
        # this path is relative to the datasets folder
        demo_path = f"{self.tasks[i].problem_folder}/{self.tasks[i].name}_demo.hdf5"
        return demo_path

    def get_task(self, i):
        return self.tasks[i]

    def get_task_emb(self, i):
        return self.task_embs[i]

    def get_task_init_states(self, i):
        init_states_path = os.path.join(
            get_libero_path("init_states"),
            self.tasks[i].problem_folder,
            self.tasks[i].init_states_file,
        )
        # init_states = torch.load(init_states_path)
        init_states = torch.load(
            init_states_path,
            map_location="cpu",       # 或 "cuda" 都行，这里随便
            weights_only=False        # 关键：显式关闭安全限制
        )
        return init_states

    def set_task_embs(self, task_embs):
        self.task_embs = task_embs


@register_benchmark
class LIBERO_SPATIAL(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_spatial"
        self._make_benchmark()


@register_benchmark
class LIBERO_OBJECT(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_object"
        self._make_benchmark()


@register_benchmark
class LIBERO_GOAL(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_goal"
        self._make_benchmark()


@register_benchmark
class LIBERO_90(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        assert (
            task_order_index == 0
        ), "[error] currently only support task order for 10-task suites"
        self.name = "libero_90"
        self._make_benchmark()


@register_benchmark
class LIBERO_10(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_10"
        self._make_benchmark()


@register_benchmark
class LIBERO_100(Benchmark):
    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = "libero_100"
        self._make_benchmark()


class _LIBERO_X_LEVEL_BASE(Benchmark):
    LEVEL = 1
    SUITE_NAME = "libero_x_level1"
    ALIASES: List[str] = []

    def __init__(self, task_order_index=0):
        super().__init__(task_order_index=task_order_index)
        self.name = self.SUITE_NAME
        self._make_benchmark()

    def _make_benchmark(self):
        self.tasks = _build_libero_x_tasks(self.LEVEL)
        self.n_tasks = len(self.tasks)


@register_benchmark
class LIBERO_X_LEVEL1(_LIBERO_X_LEVEL_BASE):
    LEVEL = 1
    SUITE_NAME = "libero_x_level1"
    ALIASES = ["libero-x-level-1", "libero_x_level_1", "libero-x-level1"]


@register_benchmark
class LIBERO_X_LEVEL2(_LIBERO_X_LEVEL_BASE):
    LEVEL = 2
    SUITE_NAME = "libero_x_level2"
    ALIASES = ["libero-x-level-2", "libero_x_level_2", "libero-x-level2"]


@register_benchmark
class LIBERO_X_LEVEL3(_LIBERO_X_LEVEL_BASE):
    LEVEL = 3
    SUITE_NAME = "libero_x_level3"
    ALIASES = ["libero-x-level-3", "libero_x_level_3", "libero-x-level3"]
