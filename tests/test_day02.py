from pathlib import Path

import pytest

from day02 import solve_part1, solve_part2, get_ranges, is_repetition, is_repetition_but_better
from utils.input import parse_lines, parse

DAY = "02"

def test_day02_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse(path)
    solution = solve_part1(input)
    assert solution == 1227775554


def test_day02_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse(path)
    solution = solve_part2(input)
    assert solution == 4174379265


@pytest.mark.parametrize(
    ("source", "prefix_length", "expected"),
    [
        ("1", 1, True),
        ("242425", 2, False),
        ("15151515", 2, True),
        ("123456123456", 6, True),
        ("12345612345" , 6 ,False)
    ]
)
def test_is_repetition_but_better(source: str, prefix_length:int, expected: bool):
    assert is_repetition_but_better(source, prefix_length) == expected

    @pytest.mark.parametrize(
        ("prefix", "number", "expected"),
        [
            (1, 1, True),
            (24, 242425, False),
            (15, 15151515, True),
            (123456, 123456123456, True),
            (123456, 12345612345, False)
        ]
    )
    def test_is_repetition(prefix: int, number: int, expected: bool):
        assert is_repetition(prefix, number) == expected
