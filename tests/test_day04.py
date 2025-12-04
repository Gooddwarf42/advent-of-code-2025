from pathlib import Path

import pytest

from day04 import solve_part1, solve_part2
from utils.input import parse_lines, parse

DAY = "04"


def test_day04_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 12


def test_day04_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 420

