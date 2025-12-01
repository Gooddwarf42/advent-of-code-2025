from pathlib import Path

from day01 import solve_part1, solve_part2
from utils.input import parse_lines


def test_day01_solve_part1() -> None:
    path = Path(__file__).parent / "01.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 3

def test_day01_solve_part2() -> None:
    path = Path(__file__).parent / "01.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 6