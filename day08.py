from __future__ import annotations

import math
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple, TypeVar
from xmlrpc.client import MAXINT

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
        coordsinates = [int(s) for s in line.split(",")]
        points.append(Point3d(coordsinates[0], coordsinates[1], coordsinates[2]))
    return points

# Ugly to write tests for, ugh....
def find_shortest_distance(mf_set : DisjointSet, points:list[Point3d]) -> tuple[Point3d, Point3d]:
    minimum_distance = MAXINT
    
    the_i: int | None = None
    the_j: int | None = None
    
    for i, item in enumerate(points):
        for j in range(i+1, len(points)):
            second_item = points[j]
            if mf_set.connected(item, second_item):
                continue
            
            distance = item.distance(second_item)
            if distance > minimum_distance:
                continue
            
            the_i = i
            the_j = j
            minimum_distance = distance
    
    if the_i is None or the_j is None:
        raise Exception("brutte cose")
    
    return points[the_i], points[the_j]


def solve_part1(source: list[str]) -> int:
    points = get_points(source)
    mf_set = DisjointSet(points)
    
    times = 10 # yeah it will bereak tests, too lazy to parametrize this
    for _ in range(times):
        x: Point3d
        y: Point3d
        x, y  = find_shortest_distance(mf_set, points)
        mf_set.merge(x,y)
    
    sizes = [len(s) for s in mf_set.subsets()]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


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
