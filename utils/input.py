from pathlib import Path

def parse(file: Path) -> str:
    with open(file) as f:
        data = f.read().strip()
        return data

def parse_lines(file: Path) -> list[str]:
    with open(file) as f:
        data = [line.rstrip("\n").strip() for line in f]
        return data