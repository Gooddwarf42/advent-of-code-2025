from dataclasses import dataclass


@dataclass()
class Range:
    lower_bound: int
    upper_bound: int

def get_ranges_from_string(source: str, ranges_separator:str) -> list[Range]:
    raw_ranges = source.split(ranges_separator)
    ranges: list[Range] = []
    for raw_range in raw_ranges:
        bounds = raw_range.split('-')
        range_to_append = Range(int(bounds[0]), int(bounds[1]))
        ranges.append(range_to_append)

    return ranges

def get_ranges_from_lines(source: list[str]) -> list[Range]:
    ranges: list[Range] = []
    for line in source:
        bounds = line.split('-')
        range_to_append = Range(int(bounds[0]), int(bounds[1]))
        ranges.append(range_to_append)

    return ranges

def is_in_bound(value: int, range: Range, lb_included:bool = True, ub_included = False) -> bool:
    excluded_lb = range.lower_bound - 1 if lb_included else range.lower_bound
    excluded_ub = range.upper_bound + 1 if ub_included else range.upper_bound
    return excluded_lb < value < excluded_ub
