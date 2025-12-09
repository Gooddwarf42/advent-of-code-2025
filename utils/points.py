from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point3d:
    x: int
    y: int
    z: int

    def distance(self: Point3d, other: Point3d) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        )


@dataclass(frozen=True)
class Point2d:
    x: int
    y: int

    def distance(self: Point2d, other: Point2d) -> float:
        return math.sqrt(
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
        )

    def rectangle_area(self: Point2d, other:Point2d) -> int:
        return abs((self.x - other.x) * (self.y - other.y))


def get_points3d(source: list[str]) -> list[Point3d]:
    points: list[Point3d] = []
    for line in source:
        coordinates = [int(s) for s in line.split(",")]
        points.append(Point3d(coordinates[0], coordinates[1], coordinates[2]))
    return points

def get_points2d(source: list[str]) -> list[Point2d]:
    points: list[Point2d] = []
    for line in source:
        coordinates = [int(s) for s in line.split(",")]
        points.append(Point2d(coordinates[0], coordinates[1]))
    return points