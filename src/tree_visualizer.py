from typing import Dict
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout


def display_resolution_tree(resolution_tree: nx.classes.DiGraph):
    _draw_resolution_tree_(resolution_tree)
    plt.show()


def _draw_resolution_tree_(tree: nx.classes.DiGraph, enable_edge_labels: bool = True, rotate_edge_labels: bool = False):
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
        edge_labels = nx.get_edge_attributes(tree, 'transformation')
        nx.draw_networkx_edge_labels(
            tree, pos=edges_pos, edge_labels=edge_labels, font_size=10, rotate=rotate_edge_labels)
