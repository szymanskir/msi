from typing import NamedTuple


class Argument(NamedTuple):
    """ Class representing an argument of a Literal.
    """
    value: str = None
    is_constant: bool = False

    def __repr__(self):
        return str(self.value)
