from typing import NamedTuple, List, Tuple

from constant import Constant
from variable import Variable
from argument import Argument

class Literal(NamedTuple):
    isNegated: bool
    arguments: Tuple[Argument] = tuple()
    name: str = ''
    @property
    def get_variables(self):
        return list(filter(lambda elm: isinstance(elm, Variable), self.arguments))

    @property
    def get_constants(self):
        return list(filter(lambda elm: isinstance(elm, Constant), self.arguments))


def negate_literal(literal: Literal) -> Literal:
    return Literal(not literal.isNegated, literal.arguments, literal.name)


def substitute_argument(argument, from_argument, to_argument):
    return to_argument if argument == from_argument else argument


def substitute_literal(literal: Literal,
                       from_argument: Argument,
                       to_argument: Argument) -> Literal:

    arguments = tuple([substitute_argument(arg, from_argument, to_argument)
                                       for arg in literal.arguments])
    return Literal(literal.isNegated, arguments, literal.name)


def find_transformation(literal1: Literal, literal2: Literal):
    transformation = dict()
    for idx in range(0, len(literal1.arguments)):
        if literal1.arguments[idx].value != literal2.arguments[idx].value:
            if literal1.arguments[idx].is_constant and literal2.arguments[idx].is_constant:
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
        
