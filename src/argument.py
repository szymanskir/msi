from typing import NamedTuple


class Argument(NamedTuple):
    key: str
    value: str = None

def is_constant(argument: Argument) -> bool:
    return argument.value is None