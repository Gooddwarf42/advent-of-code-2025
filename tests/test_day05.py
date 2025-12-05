from pathlib import Path

import pytest

from day05 import solve_part1, solve_part2, parse_day_5, actually_solve_part_1
from utils.input import parse_lines, parse
from utils.range import Range

DAY = "05"


def test_day04_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 3


def test_day04_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 14


def test_parse_day_5():
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    ranges, ids = parse_day_5(input)
    assert ranges == [
        Range(3, 5),
        Range(10, 14),
        Range(16, 20),
        Range(12, 18),
    ]

    assert ids == [1, 5, 8, 11, 17, 32]

def test_actually_solve_part_1():
    ranges = [
        Range(3,3),
    ]

    ids = [1,2,3,4,5]

    expected = 1

    assert actually_solve_part_1(ranges, ids) == expected
