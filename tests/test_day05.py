from pathlib import Path

import pytest

from day05 import solve_part1, solve_part2, parse_day_5, count_valid, weak_normalize_ranges
from utils.input import parse_lines, parse
from utils.range import Range

DAY = "05"


def test_day05_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 3


def test_day05_solve_part2() -> None:
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

@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ([Range(1, 3), Range(2, 2), Range(4, 8), Range(115, 120), ], [Range(1, 3), Range(4, 8), Range(115, 120), ]),
        ([Range(1, 100), Range(2, 2), Range(4, 8)], [Range(1, 100)]),
        ([Range(1, 3), Range(4, 5)], [Range(1, 3), Range(4, 5)]),
    ]
)
def test_weak_normalize_ranges(source: list[Range], expected: list[Range]):
    assert weak_normalize_ranges(source) == expected


def test_count_valid():
    source = [
        Range(1, 3),
        Range(4, 7),
        Range(10, 10),
        Range(115, 120),
    ]
    expected = 14
    assert count_valid(source) == 14
