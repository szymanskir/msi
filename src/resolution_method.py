from typing import List
from clause import Clause, negate_clause
from itertools import combinations

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