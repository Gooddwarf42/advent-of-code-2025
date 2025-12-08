import math

import pytest

from utils.points import Point3d


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        # Already existing ones…
        (Point3d(0, 0, 0), Point3d(0, 0, 0), 0),
        (Point3d(0, 0, 0), Point3d(1, 1, 0), math.sqrt(2)),
        (Point3d(0, 0, 0), Point3d(1, 1, 1), math.sqrt(3)),
    ]
)
def test_distance(first:Point3d, second:Point3d, expected:float):
    assert first.distance(second) == expected
