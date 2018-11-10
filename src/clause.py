from typing import NamedTuple, List, Dict
from literal import Literal, negate_literal,substitute_literal

class Clause(NamedTuple):
    literals: list

def negate_clause(clause: Clause) -> Clause:
    return Clause(list(map(negate_literal, clause.literals)))
    
# TODO: think of better argument names
def subsitute(clause: Clause, transformation: Dict) -> Clause:
    for t in transformation:
        clause = Clause(map(lambda l: substitute_literal(l, t, transformation[t]), clause.literals))
    return clause

def combine(clause_i: Clause, clause_j: Clause):
    literals_to_remove: List[Literal] = list()
    for literal_i in clause_i.literals:
        for literal_j in clause_j.literals:
            if negate_literal(literal_i) == literal_j:
                literals_to_remove += literal_i
                literals_to_remove += literal_j
    literals = set(clause_i.literals) | set(clause_j.literals) - set(literals_to_remove)
    return Clause(literals)
            