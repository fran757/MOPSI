"""Visual representation of a graph."""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani


class View:
    """Spring layout with degree visualization."""

    def __init__(self):
        self.figure, self.axis = plt.subplots()
        self.positions = {}

    def draw(self, model):
        """Draw updated graph, holding old nodes into place."""
        graph = model.graph
        ants = model.ants
        sugar = model.sugar
        nest = model.nest

        self.axis.clear()
        colors = ["w"] * len(graph.nodes)
        colors[nest] = "b"
        colors[sugar] = "r"
        for ant in ants:
            colors[ant.position] = "k"

        if not self.positions:
            self.positions = nx.spring_layout(graph)

        weights = [graph[u][v]["weight"] / 5 for u, v in graph.edges()]

        nx.draw(
            graph,
            ax=self.axis,
            pos=self.positions,
            node_size=30,
            node_color=colors,
            width=weights,
            arrows=True,
        )

    def run(self, update):
        """Run animation of given function."""
        anim = ani.FuncAnimation(self.figure, update, interval=10)
        plt.show()
