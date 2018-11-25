from typing import NamedTuple


class Argument(NamedTuple):
    """ Class representing an argument of a Literal.
    """
    value: str = None
    is_constant: bool = False

    def __str__(self):
        return str(self.value)
