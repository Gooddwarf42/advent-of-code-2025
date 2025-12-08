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

@dataclass(frozen = True)
class DistanceInfo:
    distance: float
    first_index: int
    second_index: int
    

def get_points(source: list[str]) -> list[Point3d]:
    points: list[Point3d] = []
    for line in source:
        coordsinates = [int(s) for s in line.split(",")]
        points.append(Point3d(coordsinates[0], coordsinates[1], coordsinates[2]))
    return points

def get_distance_info(points: list[Point3d]) -> list[DistanceInfo]:
    n = len(points)
    res: list[DistanceInfo] = []
    for i in range(n):
        item = points[i]
        for j in range(i + 1, n):
            second_item = points[j]
            distance = item.distance(second_item)
            res.append(DistanceInfo(distance, i, j))
            
    res.sort(key=lambda info: info.distance)
    return res

def solve_part1(source: list[str]) -> int:
    points = get_points(source)
    distances = get_distance_info(points)
    mf_set = DisjointSet(points)

    times = 1000  # yeah it will bereak tests, too lazy to parametrize this
    for i in range(times):
        distance_info = distances[i]
        first_point = points[distance_info.first_index]
        second_point =  points[distance_info.second_index]
        mf_set.merge(first_point, second_point)

    sizes = [len(s) for s in mf_set.subsets()]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def solve_part2(source: list[str]) -> int:
    points = get_points(source)
    distances = get_distance_info(points)
    mf_set = DisjointSet(points)
    
    i = 0
    while True:
        distance_info = distances[i]
        first_point = points[distance_info.first_index]
        second_point = points[distance_info.second_index]
        mf_set.merge(first_point, second_point)
        if len(mf_set.subsets()) == 1:
            break
        i = i + 1

    return first_point.x * second_point.x


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
