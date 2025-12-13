import re
import time
from dataclasses import dataclass
from pathlib import Path
from tkinter import Tk

from hypothesis.extra.array_api import DataType
from scipy.stats import false_discovery_control

from utils.input import parse_lines
from utils.list import count, parse_list_of_int
from utils.points import Point2d, get_points2d
import tkinter as tk

from utils.range import Range, is_in_bound

DAY = "10"

@dataclass(frozen=True)
class Problem:
    starting: list[bool]
    buttons: list[list[int]]
    joltages: list[int]

    def __post_init__(self):
        if len(self.starting) != len(self.joltages):
            raise ValueError(
                f"`starting` and `joltages` must have the same length "
                f"({len(self.starting)} != {len(self.joltages)})"
            )


def parse_problem(source:str) -> Problem:
    starting_pattern = "\[([^\}]*)\]"
    button_pattern = "\(([^)]*)\)"
    joltage_pattern = "\{([^}]*)\}"
    start = re.findall(starting_pattern, source)
    buttons = re.findall(button_pattern, source)
    joltages = re.findall(joltage_pattern, source)

    return Problem(
        [c == "#" for c in start[0]],
        [parse_list_of_int(group) for group in buttons],
        list(map(int, joltages[0].split(",")))
    )

def parse_problems(source: list[str]) -> list[Problem]:
    return list(map(parse_problem, source))
        

def solve_1(problem) -> int:
    return 0


def solve_part1(source: list[str]) -> int:
    problems = parse_problems(source)
    count = 0
    for problem in problems:
        count += solve_1(problem)
    return 0


def solve_part2(source: list[str]) -> int:
    return 0


if __name__ == "__main__":
    file = Path(__file__).parent / f"{DAY}.txt"
    parsed = parse_lines(file)
    start = time.perf_counter()
    result = solve_part1(parsed)
    end = time.perf_counter()
    print(f"Solved part 1 in {end - start: .6f} seconds")
    print(result)

    start = time.perf_counter()
    result = solve_part2(parsed)
    end = time.perf_counter()
    print(f"Solved part 2 in {end - start: .6f} seconds")
    print(result)
