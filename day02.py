import time
from pathlib import Path
from utils.input import parse_lines, parse
from utils.range import get_ranges

DAY = "02"


def is_repetition(prefix: int, number: int) -> bool:
    length = len(str(number))
    prefix_length = len(str(prefix))
    if length % prefix_length != 0:
        return False

    repetitions = length // prefix_length

    i = 0
    appendage = 0
    while i < repetitions:
        # add the last prefix_length digits to our partial result
        appendage = appendage + (prefix * 10 ** (i * prefix_length))

        # ensure the first i * prefix_length digits match
        if appendage != number % (10 ** (prefix_length * (i + 1))):
            return False

        i = i + 1

    return True


def is_repetition_but_better(source: str, prefix_length: int):
    length = len(source)
    if length % prefix_length != 0:
        return False

    repetitions = length // prefix_length
    prefix = source[:prefix_length]
    return prefix * repetitions == source


def solve_part1(source: str) -> int:
    count = 0
    ranges = get_ranges(source, ",")
    # let's make it stupid for now. I hate this. But I want to see part 2
    for interval in ranges:
        value = interval.lower_bound
        while value <= interval.upper_bound:
            value_string = str(value)

            length = len(value_string)
            if length % 2 != 0:
                value = value + 1
                continue

            substring_length = length // 2
            left = value_string[:substring_length]
            right = value_string[substring_length:]

            if left == right:
                count = count + value

            value = value + 1

    return count


def solve_part2(source: str) -> int:
    count = 0
    ranges = get_ranges(source, ",")
    # let's keep it stupid for now. I hate this. Maybe I'll think of something better
    for interval in ranges:
        value = interval.lower_bound
        while value <= interval.upper_bound:
            value_string = str(value)
            value_length = len(value_string)

            for i in range(1, (value_length // 2) + 1):
                if not is_repetition_but_better(value_string, i):
                    continue

                # print(f"{value} is repetition of {prefix}")
                count = count + value
                break

            value = value + 1
    return count


if __name__ == "__main__":
    file = Path(__file__).parent / f"{DAY}.txt"
    parsed = parse(file)
    start = time.perf_counter()
    result = solve_part1(parsed)
    end = time.perf_counter()
    print(f"Solved part 1 in {end - start: .6f} seconds")
    print(result)

    start = time.perf_counter()
    result = solve_part2(parsed)
    end = time.perf_counter()
    print(f"Solved part 2 in {end - start: .6f} seconds")
    print(result)
