import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines, parse

DAY = "04"

def is_oob (value:int , lb:int, ub:int) -> bool:
    """
    checks whether value is out of bounds for range between lb and ub, lb included, ub excluded
    :param value:
    :param lb:
    :param ub:
    :return:
    """
    return value < lb or value >= ub

def count_neighbours(source: list[str], i:int, j:int) -> int:
    count = 0
    cells_to_check = [
        [i-1, j-1],
        [i-1, j],
        [i-1, j+1],
        [i, j-1],
        [i, j+1],
        [i+1, j-1],
        [i+1, j],
        [i+1, j+1],
    ]

    upper_bound_i = len(source)
    upper_bound_j = len(source[0])

    for (target_i, target_j) in cells_to_check:
        if is_oob(target_i, 0, upper_bound_i) or is_oob(target_j, 0, upper_bound_j):
            continue
        cell_value = source[target_i][target_j]
        if cell_value == "@":
            count = count + 1
    return count


def solve_part1(source: list[str]) -> int:
    count = 0

    for i in range(len(source)):
        line = source[i]
        for j in range(len(line)):
            if source[i][j] != "@":
                continue
            neighbours = count_neighbours(source, i, j)
            if neighbours < 4:
                count = count + 1

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
