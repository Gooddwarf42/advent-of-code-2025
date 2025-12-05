import pytest

from utils.range import Range, get_ranges_from_string, get_ranges_from_lines, is_in_bound


def test_get_ranges():
    source = "0-7,09-15"
    result = get_ranges_from_string(source, ",")
    expected_ranges = [Range(0, 7), Range(9, 15)]
    assert result == expected_ranges


def test_get_ranges_from_lines():
    source = ["0-7", "09-15"]
    result = get_ranges_from_lines(source)
    expected_ranges = [Range(0, 7), Range(9, 15)]
    assert result == expected_ranges

@pytest.mark.parametrize(
    ("value", "lb", "ub", "lb_included", "ub_included", "expected"),
    [
        (0, 2, 4, True, True, False),
        (5, 2, 4, True, True, False),
        (2, 2, 4, True, True, True),
        (2, 2, 4, False, True, False),
        (2, 2, 4, True, False, True),
        (4, 2, 4, True, True, True),
        (4, 2, 4, False, True, True),
        (4, 2, 4, True, False, False),
        (3, 2, 4, True, True, True),
        (3, 2, 4, False, True, True),
        (3, 2, 4, True, False, True),
    ]
)
def test_is_in_bound(value, lb, ub, lb_included, ub_included, expected):
    assert is_in_bound(value, Range(lb, ub), lb_included, ub_included) ==  expected
