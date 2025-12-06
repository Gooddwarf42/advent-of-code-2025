from pathlib import Path

import pytest

from day06 import solve_part1, solve_part2
from utils.input import parse_lines, parse
from utils.range import Range

DAY = "06"


def test_day06_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 4277556


def test_day06_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 14


def test_multiply():
    assert False


def test_sanitize_line():
    assert False


def test_sanitize_input():
    assert False
