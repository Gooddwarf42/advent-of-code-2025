import pytest

from utils.list import split_list


@pytest.mark.parametrize(
    ("source", "separator", "expected"),
    [
        (["a","baba","c","","rarw"], "", [["a","baba","c"],["rarw"]]),
        ([1,2,3,4,5], 3, [[1,2], [4,5]]),
        ([1,2,3,4,5], 6, [[1,2,3,4,5]]),
        ([1,2,3,4,5], 5, [[1,2,3,4]]),
        ([1,2,3,4,5], 1, [[2,3,4,5]]),
    ]
)
def test_split_list(source, separator, expected):
    assert split_list(source, separator) == expected
