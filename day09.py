import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from utils.input import parse_lines, parse
from utils.points import Point2d, get_points2d
from utils.range import Range, get_ranges_from_lines, is_in_bound

DAY = "09"

@dataclass(frozen = True)
class AreaInfo:
    area: int
    first_index: int
    second_index: int


def get_area_info(points: list[Point2d]) -> list[AreaInfo]:
    n = len(points)
    res: list[AreaInfo] = []
    for i in range(n):
        item = points[i]
        for j in range(i + 1, n):
            second_item = points[j]
            area = item.rectangle_area(second_item)
            res.append(AreaInfo(area, i, j))

    res.sort(key=lambda info: info.area)
    return res
def solve_part1(source: list[str]) -> int:
    points =  get_points2d(source)
    area_info = get_area_info(points)

    return area_info[-1].area


def solve_part2(source: list[str]) -> int:
    points = get_points2d(source)

    max_x = max([point.x for point in points])
    max_y = max([point.y for point in points])
    print_thing = [["." for _ in range(max_y)] for _ in range(max_x)]



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
