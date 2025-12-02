from pathlib import Path

from day02 import solve_part1, solve_part2
from utils.input import parse_lines

DAY = "02"

def test_day02_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 1227775554

def test_day02_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 420