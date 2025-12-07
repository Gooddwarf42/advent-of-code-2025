import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from utils.input import parse_lines, parse
from utils.list import distinct
from utils.range import Range, get_ranges_from_lines, is_in_bound

DAY = "07"

def solve_part1(source: list[str]) -> int:
    count = 0
    beams: list[int] = [source[0].index("S")]
    
    for line in source[1:]:
        next_beams = []
        for beam_index in beams:
            if line[beam_index] != "^":
                next_beams.append(beam_index)
                continue
            
            if beam_index > 0:
                next_beams.append(beam_index - 1)

            if beam_index < len(line) - 1:
                next_beams.append(beam_index + 1)

            count = count + 1
            beams = distinct(next_beams)
            
    return count


def solve_part2(source: list[str]) -> int:
    return 0


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
