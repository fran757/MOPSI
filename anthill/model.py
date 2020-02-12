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
        self.graph = nx.grid_graph([5, 5]).to_directed()
        self.graph = nx.DiGraph()
        n = 4
        nodes = np.indices((n, n)).reshape((2, -1)).T
        neighbors = np.indices((3, 3)).reshape((2, -1)).T - 1
        self.graph.add_nodes_from([(i, j) for i, j in nodes])
        for u in nodes:
            for d in neighbors:
                if np.all(d == 0):
                    continue
                v = u + d
                if np.all(0 <= v) and np.all(v < n):
                    self.graph.add_edge(tuple(u), tuple(v))

        # self.graph = nx.erdos_renyi_graph(40, .1)#, directed=True)
        for edge in self.graph.edges(data=True):
            edge[2].update(weight=1)
        self.sugar = (n - 1, n - 1)
        self.nest = (0, 0)
        self.ants = [Ant(self.nest) for _ in range(5)]

    def reinforce(self, path):
        """Reinforce a successful path."""
        for u, v in zip(path[:-1], path[1:]):
            assert (u, v) in self.graph.edges
            self.graph[u][v]["weight"] += 1 / len(path)

    def update_ant(self, ant):
        """Move ant according to neighboring edge weights."""
        if ant.position == self.sugar:
            self.reinforce(ant.history)
            ant.reset(self.nest)
            return

        out_edges = self.graph.edges(ant.position)
        if not list(out_edges):
            if ant.position == self.nest:
                raise ValueError("nest is isolated")
            ant.reset(self.nest)
            return

        neighbors = [v for _, v in out_edges]
        weights = np.array([self.graph[u][v]["weight"] for u, v in out_edges])
        weights = weights / sum(weights)
        choice = np.random.choice(len(neighbors), p=weights)
        ant.position = neighbors[choice]

    def update(self):
        """Move ants around."""
        for ant in self.ants:
            self.update_ant(ant)


if __name__ == "__main__":
    G = Anthill()
    G.update()
