def make_spaces(size: int) -> str:
    return " " * size


def left_justify(value: str, size: int) -> str:
    return value.ljust(size + 1)[:size]
