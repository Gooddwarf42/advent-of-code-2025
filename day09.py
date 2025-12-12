import time
from dataclasses import dataclass
from pathlib import Path
from tkinter import Tk

from scipy.stats import false_discovery_control

from utils.input import parse_lines
from utils.list import count
from utils.points import Point2d, get_points2d
import tkinter as tk

from utils.range import Range, is_in_bound

DAY = "09"


@dataclass(frozen=True)
class AreaInfo:
    area: int
    first_index: int
    second_index: int


@dataclass(frozen=True)
class WallInfo:
    index: int
    ran: Range
    vertical: bool


######### DRAWING STUFF #############

def ready_canvas(points: list[Point2d], scale: float) -> tuple[Tk, tk.Canvas, list[tuple[float, float]]]:
    root: Tk = tk.Tk()
    root.title("Line Drawing Example")

    canvas = tk.Canvas(root, width=1200, height=1200, bg="white")
    canvas.pack()

    scaled_points = [(p.x * scale, p.y * scale) for p in points]
    draw_lines(canvas, scaled_points, color="blue", width=2)
    return root, canvas, scaled_points


def draw_lines(canvas, pts: list[tuple[float, float]], color="black", width=2):
    # Draw lines connecting consecutive points
    for point_one, point_two in zip(pts, pts[1:]):
        canvas.create_line(point_one[0], point_one[1], point_two[0], point_two[1], fill=color, width=width)

    canvas.create_line(pts[0][0], pts[0][1], pts[-1][0], pts[-1][1], fill=color, width=width)

    # Optional: draw the points as small circles
    r = 3
    for pt in pts:
        canvas.create_oval(pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r, fill=color)


def draw_rectangle(canvas: tk.Canvas, pts: list[tuple[float, float]], first: int, second: int, color="magenta",
                   width=2):
    marmellata = pts[first]
    giusteppe = pts[second]
    canvas.create_rectangle(marmellata[0], marmellata[1], giusteppe[0], giusteppe[1], fill=color, width=width)


#####################################


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


def find_walls(points: list[Point2d]) -> list[WallInfo]:
    walls: list[WallInfo] = []

    for i in range(len(points)):
        this_point = points[i]
        next_point = points[(i + 1) % len(points)]
        if this_point.y == next_point.y:
            # horizontal wall
            walls.append(
                WallInfo(this_point.y, Range(min(this_point.x, next_point.x), max(this_point.x, next_point.x)), False))
            continue
        walls.append(
            WallInfo(this_point.x, Range(min(this_point.y, next_point.y), max(this_point.y, next_point.y)), True))

    # Sorting all vertical walls first basically halves execution time for part 2
    walls.sort(key=lambda w: w.vertical)
    return walls


def rectangle_collides_with_wall(first_point: Point2d, second_point: Point2d, wall: WallInfo) -> bool:
    caccola = [first_point, second_point]
    max_x = max([point.x for point in caccola])
    max_y = max([point.y for point in caccola])

    min_x = min([point.x for point in caccola])
    min_y = min([point.y for point in caccola])
    if wall.vertical:
        if not min_x < wall.index < max_x:
            return False
        if wall.ran.lower_bound >= max_y:
            return False
        if wall.ran.upper_bound <= min_y:
            return False
        return True

    if not min_y < wall.index < max_y:
        return False
    if wall.ran.lower_bound >= max_x:
        return False
    if wall.ran.upper_bound <= min_x:
        return False
    return True


def solve_part1(source: list[str]) -> int:
    points = get_points2d(source)
    area_info = get_area_info(points)

    return area_info[-1].area


def solve_part2(source: list[str]) -> int:
    points = get_points2d(source)

    walls = find_walls(points)

    area_info = get_area_info(points)
    area_info.reverse()

    for info in area_info:
        is_good = True
        for wall in walls:
            if rectangle_collides_with_wall(points[info.first_index], points[info.second_index], wall):
                is_good = False
                # print(f"Collision detected: rectangle {info.first_index} - {info.second_index} collides with {wall}")
                # root, canvas, scaled_points = ready_canvas(points, scale)
                # draw_rectangle(canvas, scaled_points, info.first_index, info.second_index)
                # scaled_wall = [( wall.index * scale, wall.ran.lower_bound * scale), ( wall.index * scale, wall.ran.upper_bound * scale)] if wall.vertical else [(wall.ran.lower_bound * scale, wall.index * scale), (wall.ran.upper_bound * scale, wall.index * scale)]
                # draw_lines(canvas, scaled_wall, color="orange", width=6)
                # root.mainloop()

                break

        if not is_good:
            continue

        print(f"THIS ONE IS GOOD! {info}")

        scale = 0.0115
        root, canvas, scaled_points = ready_canvas(points, scale)
        draw_rectangle(canvas, scaled_points, info.first_index, info.second_index)
        root.mainloop()
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
