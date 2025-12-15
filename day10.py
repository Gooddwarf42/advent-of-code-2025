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


def solve_part1_problem(problem: Problem) -> int:
    final = 0
    graph : WeightedGraph[int] = create_part1_graph(problem)
    distances = graph.djikstra(final)
    return distances[problem.starting]

def solve_part2_problem(problem: Problem) -> int:
    length = len(problem.joltages)
    start = tuple([0 for _ in problem.joltages])
    #let's try with recursion with memorization
    el_cachone = { start:0 }

    gigi = 0
    def find_min_recursively(source: tuple[int, ...]) -> int:
        if source in el_cachone:
            nonlocal gigi
            gigi = gigi + 1
            if gigi % 1000000 == 0:
                print(f"cachone hittone: {source} can be done in {el_cachone[source]}")
            return el_cachone[source]

        result = MAX_INT
        for button in problem.buttons:
            updated_state = tuple([joltage - 1 if i in button else joltage for i, joltage in enumerate(source)])
            #print(f"\tChecking destination {updated_state}")
            if any(updated_state[i] < 0  for i in range(length)):
                # invalid state
                continue

            result_with_this_button = find_min_recursively(updated_state)
            if result_with_this_button < result:
                result = result_with_this_button

        if result < MAX_INT:
            print(f"scrivo el cachone: {source} can be done in {result + 1}")
        el_cachone[source] = result + 1
        return el_cachone[source]

    return find_min_recursively(problem.joltages)


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
