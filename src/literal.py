from typing import NamedTuple

from constant import Constant
from variable import Variable

class Literal(NamedTuple):
    isNegated: bool
    arguments: list
    name: str

    @property
    def get_variables(self):
        return list(filter(lambda elm: isinstance(elm, Variable), self.arguments))

    @property
    def get_constants(self):
        return list(filter(lambda elm: isinstance(elm, Constant), self.arguments))




