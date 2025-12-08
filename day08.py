from __future__ import annotations

import math
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from scipy.cluster.hierarchy import DisjointSet
from scipy.linalg import sqrtm

from utils.input import parse_lines, parse
from utils.list import distinct
from utils.points import Point3d
from utils.range import Range, get_ranges_from_lines, is_in_bound

DAY = "08"


def get_points(source: list[str]) -> list[Point3d]:
    points: list[Point3d] = []
    for line in source:
        coords = [int(s) for s in line.split(",")]
        points.append(Point3d(coords[0], coords[1], coords[2]))
    return points

def solve_part1(source: list[str]) -> int:
    sets = DisjointSet()
    return 0


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
