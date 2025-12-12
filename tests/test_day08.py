import math
from pathlib import Path

import pytest

from day08 import solve_part1, solve_part2, get_points, get_distance_info, DistanceInfo
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
    assert solution == 25272

def test_get_distance_info():
    source = [
        Point3d(0, 0, 0),
        Point3d(1, 1, 1),
        Point3d(1, 1, 2),
    ]
    expected = [
        DistanceInfo(1,1,2),
        DistanceInfo(math.sqrt(3),0,1),
        DistanceInfo(math.sqrt(6),0,2),
    ]
    assert get_distance_info(source) == expected
