from pathlib import Path

from day01 import solve
from utils.input import parse_lines


def test_day01_solve() -> None:
    path = Path(__file__).parent / "01.txt"
    input = parse_lines(path)
    solution = solve(input)
    assert solution == 3