from pathlib import Path

import pytest

from day08 import solve_part1, solve_part2, get_points
from utils.input import parse_lines, parse
from utils.points import Point3d
from utils.range import Range

DAY = "08"


def test_day08_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 40


def test_day08_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 40


def test_get_points():
    source = [
        "1,2,3",
        "4,5,6"
    ]
    expected = [
        Point3d(1,2,3),
        Point3d(4,5,6)
    ]
    assert get_points(source) == expected
