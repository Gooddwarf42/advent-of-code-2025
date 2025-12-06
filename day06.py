import re
import time
from dataclasses import dataclass
from enum import Enum
from itertools import count
from pathlib import Path
from typing import Tuple

from utils.input import parse_lines, parse
from utils.range import Range, get_ranges_from_lines, is_in_bound

DAY = "06"

def multiply(source:list[int])->int:
    acc = 1
    for value in source:
        acc = acc * value
    return acc


def sanitize_line(line:str) -> list[str]:
    return re.split("\s+", line.strip())

def sanitize_input(source: list[str]) -> tuple[list[list[int]], list[str]]:

    input_length = len(source)

    #read operators
    operators : list[str] = sanitize_line(source[-1])

    #initialize numbers, which will hold in order the operands to use
    numbers: list[list[int]] = [[] for _ in range(len(operators))]

    for line in source[:input_length - 1]:
        sanitized_line = sanitize_line(line)
        for i, value in enumerate(sanitized_line):
            numbers[i].append(int(value))

    return numbers, operators


def solve_part1(source: list[str]) -> int:
    count = 0

    numbers, operators = sanitize_input(source)

    for i, operator in enumerate(operators):
        if operator == "+":
            count = count + sum(numbers[i])
            continue
        if operator == "*":
            count = count + multiply(numbers[i])
            continue
        raise Exception("invalid operator")

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
