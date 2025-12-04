from pathlib import Path

import pytest

from day04 import solve_part1, solve_part2, count_neighbours
from utils.input import parse_lines, parse

DAY = "04"


def test_day04_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 13


def test_day04_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 420

@pytest.mark.parametrize(
    ("i", "j", "expected"),
    [
        (0, 2, 2),
        (1, 0, 2),
        (1, 3, 5),
    ]
)
def test_count_neighbours(i: int, j:int, expected: int):
    test_case = [
        "@..@@@",
        "@..@@@",
        "@..@@@",
        ]
    assert count_neighbours(test_case, i, j) == expected

