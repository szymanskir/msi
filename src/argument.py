from typing import NamedTuple


class Argument(NamedTuple):
    value: str = None
    is_constant: bool = False