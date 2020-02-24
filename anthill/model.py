"""Ants try to find a short path from nest to sugar."""

from operator import mul

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
    def __init__(self):
        self.graph = nx.Graph()
        A, B, _, C, D = [(x, 0) for x in range(4)]
        E, F = [(2, y) for y in (-2, 1)]
        self.graph.add_nodes_from([A, B, C, D, E, F])
        distances = {}
        dist = np.array([1,1,2,1,2,1]) / 2
        for (u, v), d in zip([(A, B), (B, E), (B, F), (E, C), (F, C), (C, D)], [1,1,2,1,2,1]):
            self.graph.add_edge(u, v)
            distances[(u, v)] = d
        nx.set_edge_attributes(self.graph, distances, "distance")
        nx.set_edge_attributes(self.graph, 1, "weight")

        self.nest, self.sugar = A, D
        self.ants = [Ant(self.nest) for _ in range(5)]

    def reinforce(self, path):
        """Reinforce a successful path."""
        distance = 0
        for u, v in zip(path[:-1], path[1:]):
            assert (u, v) in self.graph.edges
            distance += self.graph[u][v]["distance"]
        for u, v in zip(path[:-1], path[1:]):
            self.graph[u][v]["weight"] += 1 / distance

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

        def weight(edge):
            criteria = {"weight": 1, "distance": 0}
            u, v = edge
            result = 1
            for key, exp in criteria.items():
                result *= self.graph[u][v][key] ** exp
            return result

        weights = np.array(list(map(weight, out_edges)))
        weights = weights / sum(weights)
        choice = np.random.choice(len(neighbors), p=weights)
        ant.position = neighbors[choice]

    def update(self):
        """Move ants around."""
        for ant in self.ants:
            self.update_ant(ant)

        for edge in self.graph.edges(data=True):
            edge[2]["weight"] *= .99


if __name__ == "__main__":
    G = Anthill()
    G.update()


class Anthill:
    """A few ants try to link the nest to sugar."""

    def __init__(self):
        self.graph = nx.Graph()
        n = 4
        nodes = np.array([(i,j) for (i,j) in np.indices((n, n)).reshape((2, -1)).T if (i,j) != (2,2)])
        neighbors = np.indices((3, 3)).reshape((2, -1)).T - 1
        self.graph.add_nodes_from(list(map(tuple, nodes)))
        # self.graph.remove_node((2,2))
        distances = {}
        for u in nodes:
            for d in neighbors:
                if np.all(d == 0) or not self.graph.has_node(tuple(u + d)):
                    continue
                v = u + d
                if np.all(0 <= v) and np.all(v < n):
                    edge = (tuple(u), tuple(v))
                    self.graph.add_edge(*edge)
                    distances[edge] = np.linalg.norm(d)

        # self.graph = nx.erdos_renyi_graph(40, .1)#, directed=True)
        nx.set_edge_attributes(self.graph, distances, "distance")
        nx.set_edge_attributes(self.graph, 1, "weight")

        self.sugar = (n - 1, n - 1)
        self.nest = (0, 0)
        self.ants = [Ant(self.nest) for _ in range(5)]

    def reinforce(self, path):
        """Reinforce a successful path."""
        distance = 0
        for u, v in zip(path[:-1], path[1:]):
            assert (u, v) in self.graph.edges
            distance += self.graph[u][v]["distance"]
        for u, v in zip(path[:-1], path[1:]):
            self.graph[u][v]["weight"] += 1 / distance

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

        def weight(edge):
            criteria = {"weight": 1, "distance": 0}
            u, v = edge
            result = 1
            for key, exp in criteria.items():
                result *= self.graph[u][v][key] ** exp
            return result

        weights = np.array(list(map(weight, out_edges)))
        weights = weights / sum(weights)
        choice = np.random.choice(len(neighbors), p=weights)
        ant.position = neighbors[choice]

    def update(self):
        """Move ants around."""
        for ant in self.ants:
            self.update_ant(ant)

        for edge in self.graph.edges(data=True):
            edge[2]["weight"] *= 1


if __name__ == "__main__":
    G = Anthill()
    G.update()
