import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from utils.input import parse_lines, parse
from utils.range import Range, get_ranges_from_lines, is_in_bound

DAY = "05"


def parse_day_5(source: list[str]) -> tuple[list[Range], list[int]]:
    empty_line_index = source.index("")
    ranges = get_ranges_from_lines(source[:empty_line_index])
    item_ids = [int(s) for s in source[empty_line_index + 1:]]

    return ranges, item_ids


def actually_solve_part_1(ranges: list[Range], ids: list[int]) -> int:
    count = 0

    for id in ids:
        for range in ranges:
            if not is_in_bound(id, range, True, True):
                continue

            count = count + 1
            break

    return count


class Direction(Enum):
    OPEN = 1
    CLOSE = 2

def weak_normalize_ranges(ranges: list[Range]) -> list[Range]:
    normalized: list[Range] = []

    # badly explained idea of midnight: turn interleaved ranges into set of parentheses.
    # as long as at least a parenthesis is open, range is valid
    parenthesisms : list[tuple[int, Direction]] = []
    for r in ranges:
        parenthesisms.append((r.lower_bound, Direction.OPEN))
        parenthesisms.append((r.upper_bound, Direction.CLOSE))

    parenthesisms.sort(key=lambda gigi : gigi[0])
    count_opens = 0
    lb_to_append = None
    last_appended_ub = None
    for parenthesis in parenthesisms:
        if count_opens == 0:
            # spaghetts
            lb_to_append = parenthesis[0]
            if len(normalized) > 0 and lb_to_append == last_appended_ub:
                last = normalized.pop()
                lb_to_append = last.lower_bound

        if parenthesis[1] == Direction.OPEN:
            count_opens = count_opens + 1
        else:
            count_opens = count_opens - 1

        if count_opens == 0:
            last_appended_ub = parenthesis[0]
            normalized.append(Range(lb_to_append, last_appended_ub))

    return normalized


def count_valid(normalized: list[Range]) -> int:
    # assume input has the normalized property
    count = 0
    for r in normalized:
        count = count + (r.upper_bound - r.lower_bound + 1)
    return count


def solve_part1(source: list[str]) -> int:
    ranges, ids = parse_day_5(source)
    return actually_solve_part_1(ranges, ids)


def solve_part2(source: list[str]) -> int:
    ranges, _ = parse_day_5(source)
    normalized = weak_normalize_ranges(ranges)
    return count_valid(normalized)


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
