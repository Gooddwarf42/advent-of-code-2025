import math
from pathlib import Path

import pytest

from day10 import solve_part1, solve_part2, Problem, parse_problem, solve_part1_problem, create_part1_graph
from utils.graph import WeightedGraph
from utils.input import parse_lines, parse
from utils.points import Point3d, Point2d, get_points2d
from utils.range import Range

DAY = "10"


def test_day10_solve_part1() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part1(input)
    assert solution == 7


def test_day10_solve_part2() -> None:
    path = Path(__file__).parent / f"{DAY}.txt"
    input = parse_lines(path)
    solution = solve_part2(input)
    assert solution == 24


def test_parse_problem():
    input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    expected = Problem(
        6,
        [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]],
        [3, 5, 4, 7]
    )
    assert parse_problem(input) == expected


def test_solve():
    input = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {1,1,1,1}"
    problem = parse_problem(input)
    expected = 2
    assert solve_part1_problem(problem) == expected


def test_create_part1_graph():
    input = "[.#] (0,1) (0) {1,2}"
    problem = parse_problem(input)
    graph = WeightedGraph[int]([0, 1, 2, 3])
    graph.add_edge(0b00, 0b11, 1)
    graph.add_edge(0b11, 0b00, 1)
    graph.add_edge(0b01, 0b10, 1)
    graph.add_edge(0b10, 0b01, 1)
    graph.add_edge(0b00, 0b10, 1)
    graph.add_edge(0b10, 0b00, 1)
    graph.add_edge(0b01, 0b11, 1)
    graph.add_edge(0b11, 0b01, 1)

    assert create_part1_graph(problem) == graph
