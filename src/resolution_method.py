from itertools import combinations
from typing import Set, Tuple, Dict
import networkx as nx

from .clause import Clause, negate_clause, subsitute, combine
from .argument import Argument
from .literal import find_transformation


def resolution(knowledge_base: Set[Clause], thesis: Set[Clause]) -> Tuple[bool, nx.classes.DiGraph]:
    """Performs a resolution proof for a given knowledge_base and thesis.

    Important: All of the arguments: the knowledge_base and the thesis are
               given in clause form. The thesis is already negated.
    """
    clauses: Set[Clause] = knowledge_base | thesis
    empty_clause: Clause = Clause(frozenset())
    resolution_tree = nx.DiGraph()

    resolution_tree.add_nodes_from(clauses)

    while True:
        new: Set[Clause] = set()
        for ci, cj in combinations(clauses, 2):
            resolvents: Set[Clause] = resolve(ci, cj, resolution_tree)
            resolution_tree.add_nodes_from(resolvents)
            if empty_clause in resolvents:
                resolution_tree = reduce_resolution_tree(resolution_tree)
                return (True, resolution_tree)
            new |= resolvents
        if new < clauses:
            return (False, resolution_tree)
        clauses |= new


def resolve(clause_i: Clause, clause_j: Clause, resolution_tree=nx.DiGraph()) -> Set[Clause]:
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

                    comb = combine(new_clause_i, new_clause_j)
                    if not resolution_tree.has_node(comb):
                        trans_str = _get_transformation_string_(transformation)
                        resolution_tree.add_edge(
                            clause_i, comb, transformation=trans_str)
                        resolution_tree.add_edge(
                            clause_j, comb, transformation=trans_str)

                    resolvents.add(comb)

    return resolvents


def _get_transformation_string_(transformation: Dict[Argument, Argument]):
    if len(transformation) == 0:
        return ""

    pairs = [f"{variable}←{value}" for variable,
             value in transformation.items()]
    trans_str = ', '.join(pairs)
    return f"{{{trans_str}}}"


def reduce_resolution_tree(resolution_tree: nx.classes.DiGraph):
    empty_clause: Clause = Clause(frozenset())
    change = True
    while change:
        change = False
        nodes_to_delete = [v for v in resolution_tree.nodes(
        ) if resolution_tree.out_degree(v) == 0 and v != empty_clause]
        change = len(nodes_to_delete) > 0
        resolution_tree.remove_nodes_from(nodes_to_delete)
    return resolution_tree
