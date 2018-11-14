from itertools import combinations
from typing import Set, Tuple
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import write_dot, graphviz_layout

from .clause import Clause, negate_clause, subsitute, combine
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
            resolvents: Set[Clause] = resolve(ci, cj)
            resolution_tree.add_nodes_from(resolvents)
            resolution_tree.add_edges_from([(ci, r) for r in resolvents])
            resolution_tree.add_edges_from([(cj, r) for r in resolvents])
            if empty_clause in resolvents:
                resolution_tree = reduce_resolution_tree(resolution_tree)
                pos = graphviz_layout(resolution_tree, prog='dot')
                nx.draw(resolution_tree, pos, with_labels=True, arrows=True)
                plt.show()
                return (True, resolution_tree)
            new |= resolvents
        if new < clauses:
            return (False, resolution_tree)
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


def reduce_resolution_tree(resolution_tree: nx.classes.DiGraph):
    empty_clause: Clause = Clause(frozenset())
    change = True
    while change:
        change = False
        nodes_to_delete = [v for v in resolution_tree.nodes() if resolution_tree.out_degree(v) == 0 and v != empty_clause]
        change = len(nodes_to_delete) > 0
        resolution_tree.remove_nodes_from(nodes_to_delete)
    return resolution_tree
