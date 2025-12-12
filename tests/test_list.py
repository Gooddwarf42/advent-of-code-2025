import pytest

from utils.list import split_list, distinct, count


@pytest.mark.parametrize(
    ("source", "separator", "expected"),
    [
        (["a", "baba", "c", "", "rarw"], "", [["a", "baba", "c"], ["rarw"]]),
        ([1, 2, 3, 4, 5], 3, [[1, 2], [4, 5]]),
        ([1, 2, 3, 4, 5], 6, [[1, 2, 3, 4, 5]]),
        ([1, 2, 3, 4, 5], 5, [[1, 2, 3, 4]]),
        ([1, 2, 3, 4, 5], 1, [[2, 3, 4, 5]]),
    ]
)
def test_split_list(source, separator, expected):
    assert split_list(source, separator) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        (["a", "ba", "c", "a", ""], ["a", "ba", "c", ""]),
        ([1, 2, 3, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3, 2, 2, 3], [1, 2, 3]),
    ]
)
def test_distinct(source, expected):
    assert distinct(source) == expected


@pytest.mark.parametrize(
    ("source", "predicate", "expected"),
    [
        (["a", "ba", "c", "a", ""], lambda s: s == "", 1),
        ([1, 2, 3, 1, 2, 3], lambda i: i % 2 == 0, 2),
        ([1, 2, 3, 2, 2, 3], lambda i: True, 6),
    ]
)
def test_count(source, predicate, expected):
    assert count(source, predicate) == expected
