import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines, parse

DAY = "03"


def solve_part1(source: list[str]) -> int:
    count = 0

    for line in source:
        joltages = [int(s) for s in line]

        first_digit = -1
        second_digit = -1
        bank_length = len(joltages)
        for i in range(bank_length):
            if joltages[i] > first_digit and i < bank_length - 1: # can't have last battery of a bank as first digit
                first_digit = joltages[i]
                second_digit = joltages[i+1]
                continue
            if joltages[i] > second_digit:
                second_digit = joltages[i]

        bank_joltage = (10 * first_digit + second_digit)
        count = count + bank_joltage

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
