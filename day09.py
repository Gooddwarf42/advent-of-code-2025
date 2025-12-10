import time
from dataclasses import dataclass
from pathlib import Path

from utils.input import parse_lines
from utils.list import count
from utils.points import Point2d, get_points2d
import tkinter as tk

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

    min_x = min([point.x for point in points])
    min_y = min([point.y for point in points])

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
    for i in range(len(turns)):
        if turns[i] != turns[(i+1) % len(turns)]:
            continue
        turn_type = "L" if turns[i] == 1 else "R"
        print(f"Same turn ({turn_type}) detected at index {i}: point {points[i]}")
        evil.append([i, turn_type])

    print(len(evil))
    print(evil)
    
    # what about three times same turn?
    evil = []
    for i in range(len(turns)):
        if not(turns[i] == turns[(i+1) % len(turns)] == turns[(i+2) % len(turns)]):
            continue
        turn_type = "L" if turns[i] == 1 else "R"
        print(f"DOUBLE Same turn ({turn_type}) detected at index {i}: point {points[i]}")
        evil.append([i, turn_type])

    print(len(evil))
    print(evil)
    # Todo: find bounding rectangles (a set of bounding rectangles per corner, easily identified by their opposite vertexes)
    # iterate on all rectangles (in decreasing order of area) and check collision with any of the bounding rectangles using AABB
    # TODO uffa non penso andrà. Piango


    # drawiamo qualche cagatina
    def draw_lines(canvas, pts: list[tuple[float, float]], color="black", width=2):
        # Draw lines connecting consecutive points
        for point_one, point_two in zip(pts, pts[1:]):
            canvas.create_line(point_one[0], point_one[1], point_two[0], point_two[1], fill=color, width=width)
            
        canvas.create_line(pts[0][0], pts[0][1], pts[-1][0], pts[-1][1], fill=color, width=width)

        # Optional: draw the points as small circles
        r = 3
        for pt in pts:
            canvas.create_oval(pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r, fill=color)

    root = tk.Tk()
    root.title("Line Drawing Example")

    canvas = tk.Canvas(root, width=1200, height=1200, bg="white")
    canvas.pack()

    scale = 0.0115
    scaled_points = [(p.x * scale, p.y * scale) for p in points]
    draw_lines(canvas, scaled_points, color="blue", width=2)

    root.mainloop()



    # proviamo stupido
    area_info = get_area_info(points)
    area_info.reverse()
    print(area_info[1].area)

    for info in area_info:
        first_point = points[info.first_index]
        second_point = points[info.second_index]
        caccola = [first_point, second_point]
        max_x = max([point.x for point in caccola])
        max_y = max([point.y for point in caccola])

        min_x = min([point.x for point in caccola])
        min_y = min([point.y for point in caccola])

        predicate = lambda p : min_x < p.x < max_x and min_y < p.y < max_y
        if any(predicate(p) for p in points):
            continue

        print("this one does not have strictly internal vertexes!")
        print(first_point)
        print(second_point)
        return info.area


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
