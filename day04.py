import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines, parse

DAY = "04"

def solve_part1(source: list[str]) -> int:
    count = 0


    return count

def solve_part2(source: list[str]) -> int:
    count = 0

    return count


if __name__ == "__main__":
    file = Path(__file__).parent / f"{DAY}.txt"
    parsed = parse_lines(file)
    start = time.perf_counter()
    result = solve_part1(parsed)
    end = time.perf_counter()
    print(f"Solved part 1 in {end - start: .6f} seconds")
    print(result)

    start = time.perf_counter()
    result = solve_part2(parsed)
    end = time.perf_counter()
    print(f"Solved part 2 in {end - start: .6f} seconds")
    print(result)
