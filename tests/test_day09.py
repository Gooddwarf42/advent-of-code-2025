import math
from pathlib import Path

import pytest

from day09 import solve_part1, solve_part2, AreaInfo, get_area_info, find_vertical_walls, WallInfo
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


def test_find_vertical_walls():
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    points = get_points2d(input)
    walls = find_vertical_walls(points)
    assert walls == [
        WallInfo(2, Range(3,5)),
        WallInfo(7, Range(1,3)),
        WallInfo(9, Range(5,7)),
        WallInfo(11, Range(1,7)),
    ]
