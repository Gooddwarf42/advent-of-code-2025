from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from utils.input import parse_lines

class Direction(Enum):
    L = 1
    R = 2

def to_direction(direction_string: str) -> Direction:
    if direction_string == "L":
        return Direction.L
    if direction_string == "R":
        return Direction.R
    raise ValueError(f"Invalid direction: {direction_string}")


@dataclass
class Move:
    direction: Direction
    steps: int

def solve_part1(source: list[str]) -> int:
    count = 0
    current = 50
    for line in source:
        direction_string = line[0]
        movement_amount = int(line[1:])
        move = Move(to_direction(direction_string), movement_amount)

        # this is the closest thing to a switch case apparently
        match move.direction:
            case Direction.R:
                current = (current + move.steps) % 100
            case Direction.L:
                current = (current + 100 - move.steps) % 100

        if current == 0:
            count = count + 1

    return count


def solve_part2(source: list[str]) -> int:
    count = 0
    current = 50
    for line in source:
        direction_string = line[0]
        movement_amount = int(line[1:])
        move = Move(to_direction(direction_string), movement_amount)

        offset = 0 #just initializing, I'm lazy

        # this is the closest thing to a switch case apparently
        match move.direction:
            case Direction.R:
                offset = current
            case Direction.L:
                offset = (100 - current) % 100

        ticks = (offset + move.steps) // 100

        count = count + ticks

        # this is the closest thing to a switch case apparently
        match move.direction:
            case Direction.R:
                current = (current + move.steps) % 100
            case Direction.L:
                current = (current + 100 - move.steps) % 100

    return count


if __name__ == "__main__":
    file = Path(__file__).parent / "01.txt"
    parsed = parse_lines(file)
    result = solve_part1(parsed)
    print(result)
    result = solve_part2(parsed)
    print(result)