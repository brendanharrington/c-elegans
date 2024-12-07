import graph_tool.all as gt
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

import functions as fnc

def is_graph_connected(edges, num_nodes):
    """ c
    Check if a graph is connected.

    Parameters:
        edges (list of tuples): List of (source, target, weight) edges.
        num_nodes (int): Total number of nodes in the graph.

    Returns:
        bool: True if the graph is connected, False otherwise.
    """
    # Build adjacency list
    adjacency_list = defaultdict(list)
    for src, tgt, weight in edges:
        adjacency_list[src].append(tgt)
        adjacency_list[tgt].append(src)

    visited = set()

    def dfs(node):
        """Depth-First Search to visit nodes."""
        visited.add(node)
        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from the first node
    dfs(0)

    # Check if all nodes are visited
    return len(visited) == num_nodes

def main():
    g = gt.collection.data["celegansneural"]
    print("\nDataset for C. elegans loaded with", g.num_edges(), 'edges and', g.num_vertices(), 'vertices.')
    
    

    # edges = g.get_all_edges()
    # num_nodes = g.num_vertices()

    # connected = is_graph_connected(edges, num_nodes)
    # print("Is the graph connected?", connected)

    # d_map, d_hist = gt.label_components(g, directed=True)

    # print(d_hist)

    # fnc.print_summmary_statistics(g)
    # fnc.run_loop(g)
    
    
if __name__ == "__main__":
    main()