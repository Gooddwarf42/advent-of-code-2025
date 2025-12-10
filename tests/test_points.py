import math

import pytest
from hypothesis import given, strategies as st

from utils.points import Point3d, Point2d, get_points3d, get_points2d


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
point2d = st.builds(Point2d, st.integers(), st.integers())


@given(point3d, point3d)
def test_point3d_distance_symmetry(a: Point3d, b: Point3d):
    assert (a.distance(b) == b.distance(a))


@given(point3d, point3d)
def test_point3d_distance_positivity(a: Point3d, b: Point3d):
    assert (a.distance(b) >= 0)


@given(point3d)
def test_point3d_distance_from_self_is_zero(a: Point3d):
    assert (a.distance(a) == 0)


@given(point3d, point3d, point3d)
def test_point3d_distance_triangle_inequality(a: Point2d, b: Point2d, c: Point2d):
    ab = a.distance(b)
    bc = b.distance(c)
    ac = a.distance(c)
    assert (ab + bc >= ac)


@given(point2d, point2d)
def test_point2d_distance_symmetry(a: Point2d, b: Point2d):
    assert (a.distance(b) == b.distance(a))


@given(point2d, point2d)
def test_point2d_distance_positivity(a: Point2d, b: Point2d):
    assert (a.distance(b) >= 0)


@given(point2d)
def test_point2d_distance_from_self_is_zero(a: Point2d):
    assert (a.distance(a) == 0)


@given(point2d, point2d, point2d)
def test_point2d_distance_triangle_inequality(a: Point2d, b: Point2d, c: Point2d):
    ab = a.distance(b)
    bc = b.distance(c)
    ac = a.distance(c)
    assert (ab + bc >= ac)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (Point2d(0,0), Point2d(0,0), 0),
        (Point2d(0,0), Point2d(0,3), 0),
        (Point2d(0,0), Point2d(3,3), 9),
        (Point2d(0,0), Point2d(3,-3), 9),
    ]
)
def test_point2d_rectangle_area(a: Point2d, b: Point2d, expected: int):
    assert (a.rectangle_area(b) == expected)


@given(point2d, point2d)
def test_point2d_rectangle_area_positivity(a: Point2d, b: Point2d):
    assert (a.rectangle_area(b) >= 0)


@given(point2d, point2d)
def test_point2d_rectangle_area_symmetry(a: Point2d, b: Point2d):
    assert (a.rectangle_area(b) == b.rectangle_area(a))


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (Point2d(0,0), Point2d(0,0), 1),
        (Point2d(0,0), Point2d(0,3), 4),
        (Point2d(0,0), Point2d(3,3), 16),
        (Point2d(0,0), Point2d(3,-3), 16),
    ]
)
def test_point2d_rectangle_area_discrete(a: Point2d, b: Point2d, expected: int):
    assert (a.rectangle_area_discrete(b) == expected)


@given(point2d, point2d)
def test_point2d_rectangle_area_discrete_positivity(a: Point2d, b: Point2d):
    assert (a.rectangle_area_discrete(b) >= 0)


@given(point2d, point2d)
def test_point2d_rectangle_area_discrete_symmetry(a: Point2d, b: Point2d):
    assert (a.rectangle_area_discrete(b) == b.rectangle_area_discrete(a))


def test_get_points3d():
    source = [
        "1,2,3",
        "4,5,6"
    ]
    expected = [
        Point3d(1, 2, 3),
        Point3d(4, 5, 6)
    ]
    assert get_points3d(source) == expected


def test_get_points2d():
    source = [
        "1,2",
        "4,5"
    ]
    expected = [
        Point2d(1, 2),
        Point2d(4, 5)
    ]
    assert get_points2d(source) == expected
