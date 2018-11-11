from itertools import combinations
from typing import Set

from .clause import Clause, negate_clause, subsitute, combine
from .literal import find_transformation


def resolution(knowledge_base: Set[Clause], thesis: Clause) -> bool:
    """Performs a resolution proof for a given knowledge_base and thesis.
    """
    clauses: Set[Clause] = knowledge_base | negate_clause(thesis)
    empty_clause: Clause = Clause(frozenset())

    while True:
        new: Set[Clause] = set()
        for ci, cj in combinations(clauses, 2):
            resolvents: Set[Clause] = resolve(ci, cj)
            if empty_clause in resolvents:
                return True
            new |= resolvents
        if new < clauses:
            return False
        clauses |= new


def resolve(clause_i: Clause, clause_j: Clause) -> Set[Clause]:
    """Finds all resolvents for the given pair of clauses.
    """
    resolvents: Set[Clause] = set()
    for literal_i in clause_i.literals:
        for literal_j in clause_j.literals:
            if literal_i.name == literal_j.name and literal_i.is_negated ^ literal_j.is_negated:
                transformation = find_transformation(literal_i, literal_j)
                if transformation is None:
                    continue
                else:
                    new_clause_i = subsitute(clause_i, transformation)
                    new_clause_j = subsitute(clause_j, transformation)
                    resolvents.add(combine(new_clause_i, new_clause_j))

    return resolvents
