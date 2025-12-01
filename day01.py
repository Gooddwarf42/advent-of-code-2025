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

def solve(source: list[str]) -> int:
    count = 0
    current = 50
    for line in source:
        direction_string = line[0]
        movement_amount = int(line[1:])
        move = Move(to_direction(direction_string), movement_amount)

        # this is the closest thing to a switch case apparently
        match move.direction:
            case Direction.L:
                current = (current + move.steps) % 100
            case Direction.R:
                current = (current + 100 - move.steps) % 100

        if current == 0:
            count = count + 1

    return count



input = Path(__file__).parent / "01.txt"
result = solve(parse_lines(input))
print(result)