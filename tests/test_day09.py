import math
from pathlib import Path

import pytest

from day09 import solve_part1, solve_part2
from utils.input import parse_lines, parse
from utils.points import Point3d
from utils.range import Range

DAY = "09"


def test_day09_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 50


def test_day09_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 25272

