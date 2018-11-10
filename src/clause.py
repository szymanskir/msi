from typing import NamedTuple, List
from literal import Literal, negate_literal

class Clause(NamedTuple):
    literals: list

def negate_clause(clause: Clause) -> Clause:
    return Clause(list(map(negate_literal, clause.literals)))
    
# TODO: think of better argument names
def subsitute(clause: Clause, from_argument: str, to_argument: str) -> Clause:
    return Clause(map(lambda literal: Literal(Literal.isNegated, Literal.name)))