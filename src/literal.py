from typing import NamedTuple, Tuple, Dict

from .argument import Argument


class Literal(NamedTuple):
    """Class representing a single literal.
    """
    is_negated: bool = False
    arguments: Tuple[Argument, ...] = (Argument('X', True),)
    name: str = "literal"

    def __str__(self):
        literal_rep = '~' if self.is_negated else ''
        literal_rep += self.name
        literal_rep += f"({', '.join([str(x) for x in self.arguments])})"
        return literal_rep


def negate_literal(literal: Literal) -> Literal:
    """Negates a literal.

    Example: L(x) -> ~L(x)
    """
    return Literal(not literal.is_negated, literal.arguments, literal.name)


def substitute_argument(argument, from_argument, to_argument) -> Argument:
    return to_argument if argument == from_argument else argument


def substitute_literal(literal: Literal,
                       from_argument: Argument,
                       to_argument: Argument) -> Literal:
    """Substitures a specific argument of the literal

    Example: L(x) -> L(a) for the transformation x -> a
    """

    arguments = tuple([substitute_argument(arg, from_argument, to_argument)
                       for arg in literal.arguments])

    return Literal(literal.is_negated, arguments, literal.name)


def find_transformation(literal1: Literal, literal2: Literal) -> Dict[Argument, Argument]:
    """Finds the transformation between literals in order to perform unification. If such
    a transformation does not exist then None is returned.

    Example: (L(X), L(a)) -> (X -> a)
    """
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
