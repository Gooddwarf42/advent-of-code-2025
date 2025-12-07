from pathlib import Path

import pytest

from day07 import solve_part1, solve_part2
from utils.input import parse_lines, parse
from utils.range import Range

DAY = "07"


def test_day07_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 21


def test_day07_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 40