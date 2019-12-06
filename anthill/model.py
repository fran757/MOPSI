"""Model an evolving graph."""

import networkx as nx
import numpy as np


class Anthill:
    """First attempt of anthill simulation."""

    def __init__(self):
        self.graph = nx.erdos_renyi_graph(8, 0.5, directed=True)
        for edge in self.graph.edges(data=True):
            edge[2].update(weight=1)
        self.sugar = len(self.graph.nodes) - 1
        self.nest = 0
        self.ant = self.nest
        self.history = [self.ant]

    def update(self):
        """A new node is attached to an existing high-degree node."""
        if self.ant == self.sugar:
            for u, v in zip(self.history[:-1], self.history[1:]):
                assert (u, v) in self.graph.edges
                self.graph[u][v]["weight"] += 1 / len(self.history)
            self.ant = self.nest
            self.history = [self.ant]

        out_edges = self.graph.out_edges(self.ant)
        neighbors = [v for _, v in out_edges]
        weights = np.array([self.graph[u][v]["weight"] for u, v in out_edges])

        self.ant = np.random.choice(neighbors, p=weights / sum(weights))

        self.history.append(self.ant)
        if self.ant in self.history[:-1]:
            self.history = self.history[: self.history.index(self.ant) + 1]


if __name__ == "__main__":
    G = Anthill()
    G.update()
