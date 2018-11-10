from typing import NamedTuple, List

from constant import Constant
from variable import Variable
from argument import Argument, is_constant

class Literal(NamedTuple):
    isNegated: bool
    arguments: List[Argument]
    name: str

    @property
    def get_variables(self):
        return list(filter(lambda elm: isinstance(elm, Variable), self.arguments))

    @property
    def get_constants(self):
        return list(filter(lambda elm: isinstance(elm, Constant), self.arguments))


def negate_literal(literal: Literal) -> Literal:
    return Literal(not literal.isNegated, literal.arguments.copy(), literal.name)

def substitute_literal(literal: Literal, from_argument: str, to_argument: str) -> Literal:
    def subtitute_argument(argument, from_argument, to_argument):
        argument.
    return Literal(literal.isNegated, map(literal.arguments, literal.name)

def find_transformation(literal1: Literal, litral2:Literal):
    transformation = dict()
    for arg1, arg2, in zip(literal1, literal2):
        if is_constant(arg1) and is_constant(arg2):
            return None
        elif is_constant(arg1) and not is_constant(arg2):
            transformation[arg2] = arg1
        else is_constant(arg1)
        
