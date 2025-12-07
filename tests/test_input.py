from pathlib import Path

from utils.input import parse, parse_lines


def test_parse():
    path = Path(__file__).parent / "parse_test"
    result = parse(path)
    assert result == "martello \nconchiglia"


def test_parse_lines():
    path = Path(__file__).parent / "parse_test"
    result = parse_lines(path)
    assert result == ["martello", "conchiglia"]

def test_parse_no_strip():
    path = Path(__file__).parent / "parse_test"
    result = parse(path, False)
    assert result == "    martello \nconchiglia"

def test_parse_lines__no_strip():
    path = Path(__file__).parent / "parse_test"
    result = parse_lines(path, False)
    assert result == ["    martello ", "conchiglia"]
