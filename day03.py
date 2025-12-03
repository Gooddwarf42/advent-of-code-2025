import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines, parse

DAY = "03"

def compute_bank_joltage(bank: list[int], digits:int) -> int:
    res = 0
    current_digit = digits - 1
    last_max_index = -1
    length = len(bank)

    while current_digit >= 0:
        max_value = -1
        for i in range(last_max_index + 1, length - current_digit):
            if bank[i] <= max_value:
                continue
            max_value = bank[i]
            last_max_index = i
        res = res + (max_value * 10 ** current_digit)
        current_digit = current_digit - 1

    return res

def compute_bank_joltage_recursive(bank: list[int], digits:int) -> int:
    if digits == 1:
        return max(bank)
    enumerator = enumerate(bank[:len(bank)-digits + 1]) #iterate only on the relevant indexes
    index, value = max(enumerator, key=lambda p: p[1]) #retrieve the max in the first part of the bank
    return value * (10 ** (digits - 1)) + compute_bank_joltage_recursive(bank[(index + 1):], digits-1)


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

    for line in source:
        joltages = [int(s) for s in line]
        bank_joltage = compute_bank_joltage(joltages, 12)
        count = count + bank_joltage

    return count

def solve_part2_recursively(source: list[str]) -> int:
    count = 0

    for line in source:
        joltages = [int(s) for s in line]
        bank_joltage = compute_bank_joltage_recursive(joltages, 12)
        count = count + bank_joltage

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

    start = time.perf_counter()
    result = solve_part2_recursively(parsed)
    end = time.perf_counter()
    print(f"Solved part 2 recursively in {end - start: .6f} seconds")
    print(result)