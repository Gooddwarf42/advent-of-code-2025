import math
from pathlib import Path

import pytest

from day10 import solve_part1, solve_part2, Problem, parse_problem, solve
from utils.input import parse_lines, parse
from utils.points import Point3d, Point2d, get_points2d
from utils.range import Range

DAY = "10"


def test_day10_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 7


def test_day10_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 24


def test_parse_problem():
    input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    expected = Problem(
        ".##.",
        [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]],
        [3, 5, 4, 7]
    )
    assert parse_problem(input) == expected


def test_solve():
    input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {1,1,1,1}"
    problem = parse_problem(input)
    expected = 2
    assert solve(problem) == expected
