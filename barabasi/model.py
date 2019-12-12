"""Model an evolving graph."""

import networkx as nx
import numpy as np


class Barabasi:
    """Classic Barabasi-Albert random graph."""

    def __init__(self):
        self.graph = nx.Graph([[0, 0]])

    def update(self):
        """A new node is attached to an existing high-degree node."""
        degrees = np.array(list(self.graph.degree()))[:, 1]
        connect = np.random.choice(
            self.graph.number_of_nodes(), p=degrees / sum(degrees)
        )
        self.graph.add_edge(connect, self.graph.number_of_nodes())
