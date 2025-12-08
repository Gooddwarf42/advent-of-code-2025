import math

import pytest
from hypothesis import given, strategies as st

from utils.points import Point3d


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (Point3d(0, 0, 0), Point3d(0, 0, 0), 0),
        (Point3d(0, 0, 0), Point3d(1, 1, 0), math.sqrt(2)),
        (Point3d(0, 0, 0), Point3d(1, 1, 1), math.sqrt(3)),
    ]
)
def test_distance(first: Point3d, second: Point3d, expected: float):
    assert first.distance(second) == expected


point3d = st.builds(Point3d, st.integers(), st.integers(), st.integers())


@given(point3d, point3d)
def test_distance_symmetry(a: Point3d, b: Point3d):
    assert (a.distance(b) == b.distance(a))


@given(point3d, point3d)
def test_distance_positivity(a: Point3d, b: Point3d):
    assert (a.distance(b) >= 0)


@given(point3d)
def test_distance_from_self_is_zero(a: Point3d):
    assert (a.distance(a) == 0)


@given(point3d, point3d, point3d)
def test_distance_triangle_inequality(a:Point3d, b:Point3d, c:Point3d):
    ab = a.distance(b)
    bc = b.distance(c)
    ac = a.distance(c)
    assert (ab + bc >= ac)
