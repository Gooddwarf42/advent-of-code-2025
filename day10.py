import re
import time
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from queue import PriorityQueue, Queue
from typing import Tuple
from tkinter import Tk

from hypothesis.extra.array_api import DataType
from scipy.stats import false_discovery_control

from utils.graph import WeightedGraph, MAX_INT
from utils.input import parse_lines
from utils.list import count, parse_list_of_int
from utils.points import Point2d, get_points2d
import tkinter as tk

from utils.range import Range, is_in_bound

DAY = "10"

@dataclass(frozen=True)
class Problem:
    starting: int #using bitwise representation
    buttons: list[list[int]]
    joltages: Tuple[int, ...]

    def __post_init__(self):
        if self.starting.bit_length() > len(self.joltages):
            raise ValueError(
                f"`starting` is invalid "
                f"({bin(self.starting)} has more than {len(self.joltages)} bits)"
            )


def parse_problem(source:str) -> Problem:
    starting_pattern = "\[([^\}]*)\]"
    button_pattern = "\(([^)]*)\)"
    joltage_pattern = "\{([^}]*)\}"
    start = re.findall(starting_pattern, source)
    buttons = re.findall(button_pattern, source)
    joltages = re.findall(joltage_pattern, source)

    strart_string :str = start[0]
    start_binary_string = strart_string.replace("#", "1").replace(".", "0")

    return Problem(
        int(start_binary_string, 2),
        [parse_list_of_int(group) for group in buttons],
        tuple(map(int, joltages[0].split(",")))
    )

def parse_problems(source: list[str]) -> list[Problem]:
    return list(map(parse_problem, source))


def create_part1_graph(problem: Problem) -> WeightedGraph[int]:
    length = len(problem.joltages)
    vertexes  = [i for i in range(2 ** length)]
    graph = WeightedGraph(vertexes)
    
    for button in problem.buttons:
        change = 0
        weight = 0
        for value in button:
            index = (length - 1)- value
            change = change + 2 ** index
            weight = 1

        for vertex in vertexes:
            graph.add_edge(vertex, vertex ^ change, weight)
    
    return graph


def create_part2_graph(problem: Problem) -> WeightedGraph[Tuple[int, ...]]:
    length = len(problem.joltages)
    vertexes = [i for i in range(2 ** length)]
    graph = WeightedGraph(vertexes)

    for button in problem.buttons:
        change = 0
        weight = 0
        for value in button:
            index = (length - 1) - value
            change = change + 2 ** index
            weight = 1

        for vertex in vertexes:
            graph.add_edge(vertex, vertex ^ change, weight)

    return graph

def actually_finally_solve_part_2(buttons : list[list[int]], state : tuple[int, ...], usable_tail_length : int) -> int:
    if usable_tail_length == 1:
        last_button = buttons[-1]
        valid_value = state[last_button[0]]
        this_should_all_be_true_if_it_is_doable = [state[i] == valid_value if i in buttons else state[i] == 0 for i in range(len(state))]
        if any([not valid for valid in this_should_all_be_true_if_it_is_doable]):
            return MAX_INT
        return valid_value

    result = MAX_INT
    first_button = buttons[len(buttons) - usable_tail_length]
    max_presses = min([state[i] for i in first_button])
    for i in range(max_presses):
        updated_state = tuple([joltage - i if j in first_button else joltage for j, joltage in enumerate(state)])

        partial_result = actually_finally_solve_part_2(buttons, updated_state, usable_tail_length - 1)
        if partial_result < result:
            result = partial_result

    return min(result + 1, MAX_INT)


def solve_part1_problem(problem: Problem) -> int:
    final = 0
    graph : WeightedGraph[int] = create_part1_graph(problem)
    distances = graph.djikstra(final)
    return distances[problem.starting]

def solve_part2_problem(problem: Problem) -> int:
    length = len(problem.joltages)
    start = tuple([0 for _ in problem.joltages])
    #let's try with recursion with memorization
    # todo do that
    el_cachone = { start:0 }
    return actually_finally_solve_part_2(problem.buttons, problem.joltages, len(problem.buttons))


def solve_part1(source: list[str]) -> int:
    problems = parse_problems(source)
    count = 0
    for problem in problems:
        count += solve_part1_problem(problem)
    return count


def solve_part2(source: list[str]) -> int:
    problems = parse_problems(source)
    count = 0
    i = 1
    for problem in problems:
        print(f"solving problem {i}/{len(source)}...")
        count += solve_part2_problem(problem)
        print(f"solved problem {i}!")
        i = i + 1

    return count


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
