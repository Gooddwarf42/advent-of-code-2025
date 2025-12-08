from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
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

