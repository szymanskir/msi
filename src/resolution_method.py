from typing import List
from clause import Clause, negate_clause, subsitute, combine
from itertools import combinations
from literal import find_transformation

def resolution(knowledge_base: List[Clause], thesis: Clause) -> bool:
    clauses: List[Clause] = knowledge_base + negate_clause(thesis)

    while True:
        new: List[Clause] = list()
        for ci, cj in combinations(clauses, 2):
            resolvents: List[Clause] = resolve(ci, cj)
            if None in resolvents:
                return True
            new += resolvents
        if set(new) < set(clauses):
            return False
        clauses += new


def resolve(clause_i: Clause, clause_j: Clause) -> List[Clause]:
    resolvents: List[Clause] = list()
    for literal_i in clause_i.literals:
        for literal_j in clause_j.literals:
            if literal_i.name == literal_j.name and literal_i.isNegated ^ literal_j.isNegated:
                transformation = find_transformation(literal_i, literal_j)
                if transformation is None:
                    continue
                else:
                    new_clause_i = subsitute(clause_i, transformation)
                    new_clause_j = subsitute(clause_j, transformation)
                    resolvents += (combine(new_clause_i, new_clause_j),)
    return resolvents
