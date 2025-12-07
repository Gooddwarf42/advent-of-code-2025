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

    bounds = Range(0, len(source[0]))
    
    for line in source[1:]:
        next_beams = []
        for beam_index in beams:
            if line[beam_index] != "^":
                next_beams.append(beam_index)
                continue

            for neighbour in (beam_index + 1, beam_index - 1):
                if not is_in_bound(neighbour, bounds):
                    continue
                next_beams.append(neighbour)
            
            count = count + 1
        
        beams = distinct(next_beams)
            
    return count


def solve_part2(source: list[str]) -> int:
    starting_beam_index = source[0].index("S")
    beams: dict[int, int] = {starting_beam_index: 1} 
    bounds = Range(0, len(source[0]))
    for line in source[1:]:
        current_beams = beams.copy() #makes a shallow copy, so we don't do weird shit when iterating
        for beam_index, timelines in current_beams.items():
            if line[beam_index] != "^":
                continue

            for neighbour in (beam_index + 1, beam_index - 1):
                if not is_in_bound(neighbour, bounds):
                    continue
                # we are modifying the (timelines) values of the dictionary we are iterating on!
                # this is sketchy, but if you think hard about it for a moment, you can
                # convince yourself that it is safe.
                beams[neighbour] = timelines + beams.get(neighbour, 0)
                
            beams.pop(beam_index)
            
    return sum(beams.values())


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
