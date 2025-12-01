import pytest

from utils.first_tests import somma_testolosa

@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (3, 5, 8),
        (2, 2, 4),
        (-1, -1, -2),
        (0,0,0)
    ]
)
def test_somma_testolosa(a:int, b:int, expected:int) -> None:
    result = somma_testolosa(a,b)
    assert result == expected
