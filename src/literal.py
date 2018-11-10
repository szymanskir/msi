from typing import NamedTuple, List, Tuple

from constant import Constant
from variable import Variable
from argument import Argument

class Literal(NamedTuple):
    isNegated: bool
    arguments: Tuple[Argument]
    name: str

    @property
    def get_variables(self):
        return list(filter(lambda elm: isinstance(elm, Variable), self.arguments))

    @property
    def get_constants(self):
        return list(filter(lambda elm: isinstance(elm, Constant), self.arguments))


def negate_literal(literal: Literal) -> Literal:
    return Literal(not literal.isNegated, literal.arguments, literal.name)

def substitute_literal(literal: Literal, from_argument: str, to_argument: str) -> Literal:
    def subtitute_argument(argument, from_argument, to_argument):
        return to_argument if argument == from_argument else argument
    return Literal(literal.isNegated, map(subtitute_argument, literal.arguments))


def find_transformation(literal1: Literal, literal2:Literal):
    transformation = dict()
    for idx in range(0, literal1.arguments.count):
        if literal1.arguments[idx].value != literal2.arguments[idx].value:
            if literal1.arguments[idx].is_constant and literal2.argument[idx].is_constant:
                return None
            elif literal1.arguments[idx].is_constant:
                replaced_variable = literal2.arguments[idx]
                value = literal1.arguments[idx]
            elif literal2.arguments[idx].is_constant:
                replaced_variable = literal1.arguments[idx]
                value = literal2.arguments[idx]
            else:
                replaced_variable = literal1.arguments[idx]
                value = literal2.arguments[idx]
            transformation[replaced_variable] = value
            literal1 = substitute_literal(literal1, replaced_variable, value)
            literal2 = substitute_literal(literal2, replaced_variable, value)
    return transformation
        
