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
            resolvents: Set[Clause] = resolve(ci, cj, resolution_tree)
            resolution_tree.add_nodes_from(resolvents)
            if empty_clause in resolvents:
                resolution_tree = reduce_resolution_tree(resolution_tree)
                draw_resolution_tree(resolution_tree)
                return (True, resolution_tree)
            new |= resolvents
        if new < clauses:
            return (False, resolution_tree)
        clauses |= new


def resolve(clause_i: Clause, clause_j: Clause, resolution_tree) -> Set[Clause]:
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
                    trans_str = _get_transformation_string_(transformation)
                    resolution_tree.add_edge(
                        clause_i, comb, subst=trans_str)
                    resolution_tree.add_edge(
                        clause_j, comb, subst=trans_str)

                    resolvents.add(comb)

    return resolvents


def _get_transformation_string_(transformation):
    if len(transformation) == 0:
        return ""

    pairs = [f"{variable}: {value}" for variable,
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


def draw_resolution_tree(tree, enable_edge_labels=True):
    plt.figure()

    # graph
    nodes_pos = graphviz_layout(tree, prog='dot')
    nx.draw(tree, nodes_pos,
            node_size=150, edge_color='#7d7d7d')

    # nodes labels
    pos_attrs = {}
    for node, coords in nodes_pos.items():
        pos_attrs[node] = (coords[0], coords[1] - 6)

    custom_node_attrs = {}
    for node, attr in tree.nodes.items():
        custom_node_attrs[node] = str(node)

    nodes_bbox = dict(fc="w", lw=0.1)
    nx.draw_networkx_labels(
        tree, pos_attrs, labels=custom_node_attrs, font_size=10, bbox=nodes_bbox)

    # edge labels
    if(enable_edge_labels):
        edges_pos = graphviz_layout(tree, prog='dot')
        edge_labels = nx.get_edge_attributes(tree, 'subst')
        nx.draw_networkx_edge_labels(
            tree, pos=edges_pos, edge_labels=edge_labels, font_size=10)

    plt.show()
