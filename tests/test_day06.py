from pathlib import Path

import pytest

from day06 import solve_part1, solve_part2, multiply, sanitize_line, sanitize_input, sanitize_input_part_2
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
    input = parse_lines(path, False)
    solution = solve_part2(input)
    assert solution == 3263827


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ([], 1),
        ([2, 4], 8),
        ([5, -4, 3], -60),
    ]
)
def test_multiply(source: list[int], expected: int):
    assert multiply(source) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("a   b  c", ["a", "b", "c"]),
        ("            v", ["v"]),
        (" v ", ["v"]),
    ]
)
def test_sanitize_line(source: str, expected: list[str]):
    assert sanitize_line(source) == expected


def test_sanitize_input():
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path, False)
    sanitized = sanitize_input(input)
    assert sanitized == ([[123, 45, 6], [328, 64, 98], [51, 387, 215], [64, 23, 314]], ["*", "+", "*", "+"])


def test_sanitize_input_part_2():
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path, False)
    sanitized = sanitize_input_part_2(input)
    assert sanitized == ([[1, 24, 356], [369, 248, 8], [32, 581, 175], [623, 431, 4]], ["*", "+", "*", "+"])
