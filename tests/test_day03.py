from pathlib import Path

import pytest

from day03 import solve_part1, solve_part2, compute_bank_joltage, compute_bank_joltage_recursive
from utils.input import parse_lines, parse

DAY = "03"


def test_day03_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 357


def test_day03_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 3121910778619


@pytest.mark.parametrize(
    ("bank_string", "digits", "expected"),
    [
        ("7856", 2, 86),
        ("21432", 3, 432),
        ("21432", 4, 2432),
    ]
)
def test_compute_bank_joltage(bank_string: str, digits: int, expected:int):
    bank = [int(s) for s in bank_string]
    assert compute_bank_joltage(bank, digits) == expected

@pytest.mark.parametrize(
    ("bank_string", "digits", "expected"),
    [
        ("7856", 2, 86),
        ("21432", 3, 432),
        ("21432", 4, 2432),
    ]
)
def test_compute_bank_joltage_recursive(bank_string: str, digits: int, expected: int):
    bank = [int(s) for s in bank_string]
    assert compute_bank_joltage_recursive(bank, digits) == expected
