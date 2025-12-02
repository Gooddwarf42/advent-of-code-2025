from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines, parse

DAY = "02"


@dataclass()
class Range:
    lower_bound: int
    upper_bound: int


def get_ranges(source: str) -> list[Range]:
    raw_ranges = source.split(',')
    ranges: list[Range] = []
    for raw_range in raw_ranges:
        bounds = raw_range.split('-')
        range_to_append = Range(int(bounds[0]), int(bounds[1]))
        ranges.append(range_to_append)

    return ranges


def solve_part1(source: str) -> int:
    count = 0
    ranges = get_ranges(source)
    # let's make it stupid for now. I hate this. But I want to see part 2
    for interval in ranges:
        value = interval.lower_bound
        while value <= interval.upper_bound:
            value_string = str(value)

            length = len(value_string)
            if length % 2 != 0:
                value = value + 1
                continue

            substring_length = length // 2
            left = value_string[:substring_length]
            right = value_string[substring_length:]

            if left == right:
                count = count + value

            value = value + 1

    return count


def solve_part2(source: str) -> int:
    count = 0

    return count

if __name__ == "__main__":
    file = Path(__file__).parent / f"{DAY}.txt"
    parsed = parse(file)
    result = solve_part1(parsed)
    print(result)
    result = solve_part2(parsed)
    print(result)
