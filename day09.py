import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from utils.input import parse_lines, parse
from utils.list import count
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
            area = item.rectangle_area_discrete(second_item)
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

    min_x = max([point.x for point in points])
    min_y = max([point.y for point in points])

    on_top = count(points, lambda p: p.y == min_y)
    on_left = count(points, lambda p: p.x == min_x)
    on_bottom = count(points, lambda p: p.y == max_y)
    on_right = count(points, lambda p: p.x == max_x)


    print([on_top, on_left, on_right, on_bottom])
    # this gives us [2,2,2,2]. We can rid of some annoying edge cases then!

    # just for the sake of more edge case avoidance, I wanna see if we alternate left and right turns
    turns: list[int] = []
    for i in range(len(points)):
        this_point = points[i]
        next_point = points[(i+1) % len(points)]
        prev_point = points[(len(points)+ i - 1) % len(points)]
        vec_prev = [prev_point.x - this_point.x, prev_point.y - this_point.y]
        vec_next = [next_point.x - this_point.x, next_point.y - this_point.y]
        turn = vec_prev[0] * vec_next[1] - vec_prev[1] * vec_next[0]
        turns.append(abs(turn)//turn)


    evil = []
    for i in range(len(turns) - 1):
        if turns[i] != turns[(i+1) % len(turns)]:
            continue
        turn_type = "L" if turns[i] == 1 else "R"
        print(f"Same turn ({turn_type}) detected at index {i}: point {points[i]}")
        evil.append([i, turn_type])

    print(len(evil))
    print(evil)
    # Todo: find bounding rectangles (a set of bounding rectangles per corner, easily identified by their opposite vertexes)
    # iterate on all rectangles (in decreasing order of area) and check collision with any of the bounding rectangles using AABB
    # TODO uffa non penso andrà. Piango


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
