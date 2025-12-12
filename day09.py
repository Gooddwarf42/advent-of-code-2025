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

def draw_rectangle(canvas: tk.Canvas, pts: list[tuple[float, float]], first: int, second: int, color="magenta", width=2):
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


def find_vertical_walls(points: list[Point2d]) -> list[WallInfo]:
    walls: list[WallInfo] = []

    for i in range(len(points)):
        this_point = points[i]
        next_point = points[(i + 1) % len(points)]
        if this_point.y == next_point.y:
            # horizontal wall
            continue
        walls.append(WallInfo(this_point.x, Range(min(this_point.y, next_point.y), max(this_point.y, next_point.y))))

    walls.sort(key=lambda info: info.index)
    return walls

def find_horizontal_walls(points: list[Point2d]) -> list[WallInfo]:
    walls: list[WallInfo] = []

    for i in range(len(points)):
        this_point = points[i]
        next_point = points[(i + 1) % len(points)]
        if this_point.x == next_point.x:
            # horizontal wall
            continue
        walls.append(WallInfo(this_point.y, Range(min(this_point.x, next_point.x), max(this_point.x, next_point.x))))

    walls.sort(key=lambda info: info.index)
    return walls


def is_wall_on_left(wall: WallInfo, point: Point2d) -> bool:
    if wall.index >= point.x:
        return False
    return is_in_bound(point.y, wall.ran, False, True)


def is_wall_on_right(wall: WallInfo, point: Point2d) -> bool:
    if wall.index <= point.x:
        return False
    return is_in_bound(point.y, wall.ran, False, True)

def has_wall_on_left(wall: WallInfo, walls: list[WallInfo]) -> bool:
    def is_wall_on_left_of_a_wall(source:WallInfo, target: WallInfo) -> bool:
        if target.index >= source.index:
            return False
        if target.ran.lower_bound >= source.ran.upper_bound:
            return False
        if target.ran.upper_bound <= source.ran.lower_bound:
            return  False
        return True

    walls_on_left= count(walls, lambda w: is_wall_on_left_of_a_wall(wall, w))
    return walls_on_left > 0

def has_wall_on_right(wall: WallInfo, walls: list[WallInfo]) -> bool:
    def is_wall_on_right_of_a_wall(source:WallInfo, target: WallInfo) -> bool:
        if target.index <= source.index:
            return False
        if target.ran.lower_bound >= source.ran.upper_bound:
            return False
        if target.ran.upper_bound <= source.ran.lower_bound:
            return  False
        return True

    walls_on_right= count(walls, lambda w: is_wall_on_right_of_a_wall(wall, w))
    return walls_on_right > 0


def solve_part1(source: list[str]) -> int:
    points = get_points2d(source)
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
        next_point = points[(i + 1) % len(points)]
        prev_point = points[(len(points) + i - 1) % len(points)]
        vec_prev = [prev_point.x - this_point.x, prev_point.y - this_point.y]
        vec_next = [next_point.x - this_point.x, next_point.y - this_point.y]
        turn = vec_prev[0] * vec_next[1] - vec_prev[1] * vec_next[0]
        turns.append(abs(turn) // turn)

    evil = []
    for i in range(len(turns)):
        if turns[i] != turns[(i + 1) % len(turns)]:
            continue
        turn_type = "L" if turns[i] == 1 else "R"
        print(f"Same turn ({turn_type}) detected at index {i}: point {points[i]}")
        evil.append([i, turn_type])

    print(len(evil))
    print(evil)

    # what about three times same turn?
    evil = []
    for i in range(len(turns)):
        if not (turns[i] == turns[(i + 1) % len(turns)] == turns[(i + 2) % len(turns)]):
            continue
        turn_type = "L" if turns[i] == 1 else "R"
        print(f"DOUBLE Same turn ({turn_type}) detected at index {i}: point {points[i]}")
        evil.append([i, turn_type])

    print(len(evil))
    print(evil)
    # Todo: find bounding rectangles (a set of bounding rectangles per corner, easily identified by their opposite vertexes)
    # iterate on all rectangles (in decreasing order of area) and check collision with any of the bounding rectangles using AABB
    # TODO uffa non penso andrà. Piango

    vertical_walls = find_vertical_walls(points)
    good_left_walls: list[WallInfo] = []
    good_right_walls: list[WallInfo] = []
    for wall in vertical_walls:
        if not has_wall_on_left(wall, vertical_walls):
            good_left_walls.append(wall)
            continue
        if not has_wall_on_right(wall, vertical_walls):
            good_right_walls.append(wall)
            continue


    horizontal_walls = find_horizontal_walls(points)
    good_top_walls: list[WallInfo] = []
    good_bottom_walls: list[WallInfo] = []
    for wall in horizontal_walls:
        if not has_wall_on_left(wall, horizontal_walls):
            good_top_walls.append(wall)
            continue
        if not has_wall_on_right(wall, horizontal_walls):
            good_bottom_walls.append(wall)
            continue

    # drawiamo qualche cagatina
    scale = 0.0115
    #scale = 30.0
    root, canvas, scaled_points = ready_canvas(points, scale)

    scaled_vert_walls = [[(wall.index * scale, wall.ran.lower_bound * scale), (wall.index * scale, wall.ran.upper_bound * scale)] for wall in vertical_walls]
    for scaled_wall in scaled_vert_walls:
        draw_lines(canvas, scaled_wall, color="red", width=1)

    scaled_good_left_vert_walls = [[(wall.index * scale, wall.ran.lower_bound * scale), (wall.index * scale, wall.ran.upper_bound * scale)] for wall in good_left_walls]
    for scaled_wall in scaled_good_left_vert_walls:
        draw_lines(canvas, scaled_wall, color="green", width=6)

    scaled_good_right_vert_walls = [[(wall.index * scale, wall.ran.lower_bound * scale), (wall.index * scale, wall.ran.upper_bound * scale)] for wall in good_right_walls]
    for scaled_wall in scaled_good_right_vert_walls:
        draw_lines(canvas, scaled_wall, color="orange", width=6)
        
    scaled_hor_walls = [[(wall.ran.lower_bound * scale, wall.index * scale), (wall.ran.upper_bound * scale, wall.index * scale)] for wall in horizontal_walls]
    for scaled_wall in scaled_hor_walls:
        draw_lines(canvas, scaled_wall, color="red", width=1)

    scaled_good_left_hor_walls = [[(wall.ran.lower_bound * scale, wall.index * scale,), (wall.ran.upper_bound * scale, wall.index * scale)] for wall in good_top_walls]
    for scaled_wall in scaled_good_left_hor_walls:
        draw_lines(canvas, scaled_wall, color="green", width=6)

    scaled_good_right_hor_walls = [[(wall.ran.lower_bound * scale, wall.index * scale), (wall.ran.upper_bound * scale, wall.index * scale,)] for wall in good_bottom_walls]
    for scaled_wall in scaled_good_right_hor_walls:
        draw_lines(canvas, scaled_wall, color="orange", width=6)

    root.mainloop()

    # proviamo
    area_info = get_area_info(points)
    area_info.reverse()

    el_cachone: dict[Point2d, bool] = {}

    for info in area_info:
        root, canvas, scaled_points = ready_canvas(points, scale)
        draw_rectangle(canvas, scaled_points, info.first_index, info.second_index)
        root.mainloop()

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
