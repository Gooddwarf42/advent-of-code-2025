from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines

DAY = "02"


def solve_part1(source: list[str]) -> int:
    count = 0


    return count


def solve_part2(source: list[str]) -> int:
    count = 0


    return count



file = Path(__file__).parent / f"{DAY}.txt"
parsed = parse_lines(file)
result = solve_part1(parsed)
print(result)
result = solve_part2(parsed)
print(result)