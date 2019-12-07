"""Ants try to find a short path from nest to sugar."""

import networkx as nx
import numpy as np


class Ant:
    """Ant knows its position and history."""
    def __init__(self, position):
        self.history = []
        self.position = position

    @property
    def position(self):
        """Current position is last in history."""
        return self.history[-1]

    @position.setter
    def position(self, value):
        """A closed loop can be forgotten."""
        if value in self.history:
            self.history = self.history[: self.history.index(value)]
        self.history.append(value)

    def reset(self, position):
        """Forget everything and start back in position."""
        self.history = []
        self.position = position


class Anthill:
    """A few ants try to link the nest to sugar."""

    def __init__(self):
        self.graph = nx.erdos_renyi_graph(20, 0.3, directed=True)
        for edge in self.graph.edges(data=True):
            edge[2].update(weight=1)
        self.sugar = len(self.graph.nodes) - 1
        self.nest = 0
        self.ants = [Ant(self.nest) for _ in range(5)]

    def reinforce(self, path):
        """Reinforce a successful path."""
        for u, v in zip(path[:-1], path[1:]):
            assert (u, v) in self.graph.edges
            self.graph[u][v]["weight"] += 1 / len(path)

    def update_ant(self, ant):
        """Move ant according to neighboring edge weights.
        Upon reaching sugar or getting stuck, ant immediately gets back to work.
        """
        if ant.position == self.sugar:
            self.reinforce(ant.history)
            ant.reset(self.nest)
            # return

        out_edges = self.graph.out_edges(ant.position)
        if not out_edges:
            ant.reset(self.nest)
            # return

        neighbors = [v for _, v in out_edges]
        weights = np.array([self.graph[u][v]["weight"] for u, v in out_edges])

        ant.position = np.random.choice(neighbors, p=weights / sum(weights))

    def update(self):
        """Move ants around."""
        for ant in self.ants:
            self.update_ant(ant)


if __name__ == "__main__":
    G = Anthill()
    G.update()
