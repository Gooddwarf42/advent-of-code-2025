from pathlib import Path

from utils.input import parse, parse_lines


def test_parse():
    path = Path(__file__).parent / "parse_test.txt"
    result = parse(path)
    assert result == "martello\nconchiglia"


def test_parse_lines():
    path = Path(__file__).parent / "parse_test.txt"
    result = parse_lines(path)
    assert result == ["martello", "conchiglia"]
