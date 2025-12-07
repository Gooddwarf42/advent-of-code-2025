from typing import TypeVar

T = TypeVar("T")
def split_list(source: list[T], separator: T) -> list[list[T]]:
    result = []
    current_group = []
    for item in source:
        if item != separator:
            current_group.append(item)
            continue

        # avoid prefix empty group in case we start with (any amount of) separators
        if result == [] and current_group == []:
             continue

        result.append(current_group)
        current_group = []

    # Sorry, the if current_group: syntax is too ugly for me to bear.
    if current_group != []:
        result.append(current_group)

    return result
