from pathlib import Path

def parse(file: Path, should_strip:bool = True) -> str:
    with open(file, "r") as f:
        data = f.read()

        if should_strip:
            data = data.strip()

        return data

def parse_lines(file: Path, should_strip:bool = True) -> list[str]:
    with open(file, "r") as f:
        data = [line.rstrip("\n").strip() if should_strip else line.rstrip("\n") for line in f]
        return data