"""Model an evolving graph."""

import networkx as nx
import numpy as np


class Barabasi:
    """Classic Barabasi-Albert random graph."""

    def __init__(self):
        self.graph = nx.Graph([[0, 0]])

    def update(self):
        """A new node is attached to an existing high-degree node."""
        degrees = np.array([len(adj[1]) for adj in self.graph.adjacency()])
        n = self.graph.number_of_nodes()
        connect = np.random.choice(n, p=degrees / sum(degrees))
        self.graph.add_edge(connect, n)
        return self.graph
