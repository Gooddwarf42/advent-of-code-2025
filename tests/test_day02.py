from pathlib import Path

from day02 import solve_part1, solve_part2, get_ranges, Range
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
    assert solution == 420


def test_get_ranges():
    source = "0-7,09-15"
    result = get_ranges(source)
    expected_ranges = [Range(0, 7), Range(9, 15)]
    assert result == expected_ranges
