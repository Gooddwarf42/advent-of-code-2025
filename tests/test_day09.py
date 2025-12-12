import math
from pathlib import Path

import pytest

from day09 import solve_part1, solve_part2, AreaInfo, get_area_info, find_vertical_walls, WallInfo, is_wall_on_left, is_wall_on_right, has_wall_on_left, has_wall_on_right
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
        WallInfo(2, Range(3, 5)),
        WallInfo(7, Range(1, 3)),
        WallInfo(9, Range(5, 7)),
        WallInfo(11, Range(1, 7)),
    ]


@pytest.mark.parametrize(
    ("wall", "point", "expected"),
    [
        (WallInfo(1, Range(2, 3), True), Point2d(2, 2), True),
        (WallInfo(3, Range(2, 3), True), Point2d(2, 2), False),
        (WallInfo(2, Range(2, 3), True), Point2d(2, 2), False),
        (WallInfo(1, Range(2, 3), True), Point2d(2, 1), False),
        (WallInfo(1, Range(2, 3), True), Point2d(2, 3), True),
    ]
)
def test_is_wall_on_left(wall: WallInfo, point: Point2d, expected: bool):
    assert is_wall_on_left(wall, point) == expected


@pytest.mark.parametrize(
    ("wall", "point", "expected"),
    [
        (WallInfo(1, Range(2, 3), True), Point2d(2, 2), False),
        (WallInfo(3, Range(2, 3), True), Point2d(2, 2), True),
        (WallInfo(2, Range(2, 3), True), Point2d(2, 2), False),
        (WallInfo(3, Range(2, 3), True), Point2d(2, 1), False),
        (WallInfo(3, Range(2, 3), True), Point2d(2, 3), True),
        (WallInfo(3, Range(2, 3), True), Point2d(2, 3), True),
    ]
)
def test_is_wall_on_right(wall: WallInfo, point: Point2d, expected: bool):
    assert is_wall_on_right(wall, point) == expected

@pytest.mark.parametrize(
    ("wall", "walls", "expected"),
    [
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(2, 3), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(0, 1), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(0, 2), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(3, 4), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(4, 5), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(1, Range(2, 3), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(2, 3), True)], False),
    ]
)
def test_has_wall_on_left(wall: WallInfo, walls: list[WallInfo], expected: bool):
    assert has_wall_on_left(wall, walls) == expected

@pytest.mark.parametrize(
    ("wall", "walls", "expected"),
    [
        (WallInfo(1, Range(2, 3), True), [WallInfo(0, Range(2, 3), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(1, Range(2, 3), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(2, 3), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(0, 1), True)], False),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(0, 2), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(3, 4), True)], True),
        (WallInfo(1, Range(2, 3), True), [WallInfo(2, Range(4, 5), True)], False),
    ]
)
def test_has_wall_on_right(wall: WallInfo, walls: list[WallInfo], expected: bool):
    assert has_wall_on_right(wall, walls) == expected
