import math
from pathlib import Path

import pytest

from day09 import solve_part1, solve_part2, AreaInfo, get_area_info, WallInfo, find_walls
from utils.input import parse_lines, parse
from utils.points import Point3d, Point2d, get_points2d
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
    assert solution == 24


def test_get_area_info():
    source = [
        Point2d(0, 0),
        Point2d(1, 1),
        Point2d(1, 2),
    ]
    expected = [
        AreaInfo(0, 1, 2),
        AreaInfo(1, 0, 1),
        AreaInfo(2, 0, 2),
    ]
    assert get_area_info(source) == expected