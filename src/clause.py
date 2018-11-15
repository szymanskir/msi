from typing import NamedTuple, FrozenSet, Dict, Set

from .argument import Argument
from .literal import Literal, negate_literal, substitute_literal


class Clause(NamedTuple):
    literals: FrozenSet[Literal]

    def __repr__(self):
        if(not self.literals):
            return "∅"

        return ' ∨ '.join([str(x) for x in self.literals])


def negate_clause(clause: Clause) -> FrozenSet[Clause]:
    """Negates a clause and returns a set of clauses.

    Example: A | B | C -> {~A, ~B, ~C}
    """
    negated_literals = [[negate_literal(literal)]
                        for literal in clause.literals]
    return frozenset([Clause(frozenset(l)) for l in negated_literals])


def subsitute(clause: Clause, transformation: Dict[Argument, Argument]) -> Clause:
    """Applies given transformations to the clause.

    Example: X -> a for P(X) will result in P(a)
    """
    for t in transformation:
        clause = Clause(
            frozenset([substitute_literal(l, t, transformation[t])
                       for l in clause.literals])
        )
    return clause


def combine(clause_i: Clause, clause_j: Clause) -> Clause:
    """ Combines the given pair of clauses. It is equivalent to the or operation.
    It used mainly to reduce opposite literals.

    Example: combine(A | B | C, ~A) =  B | C 
    """
    literals_to_remove: Set[Literal] = set()
    for literal_i in clause_i.literals:
        for literal_j in clause_j.literals:
            if negate_literal(literal_i) == literal_j:
                literals_to_remove.add(literal_i)
                literals_to_remove.add(literal_j)
    literals = (clause_i.literals | clause_j.literals) - (literals_to_remove)

    return Clause(frozenset(literals))
