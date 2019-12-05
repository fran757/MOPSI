"""Visual representation of a graph."""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani


class View:
    """Spring layout with degree visualization."""

    def __init__(self):
        self.figure, self.axis = plt.subplots()
        self.positions = {}
        self.old_nodes = []

    def draw(self, graph):
        """Draw updated graph, holding old nodes into place."""
        self.axis.clear()
        degrees = [len(adj[1]) for adj in graph.adjacency()]

        hold = {}
        if self.positions:
            hold.update(pos=self.positions, fixed=self.old_nodes)
        self.positions = nx.spring_layout(graph, **hold)

        nx.draw(
            graph,
            ax=self.axis,
            pos=self.positions,
            node_size=50,
            node_color=degrees,
            cmap=plt.cm.bwr,
        )
        self.old_nodes = list(graph.nodes)

    def run(self, update):
        """Run animation of given function."""
        anim = ani.FuncAnimation(self.figure, update, interval=50)
        plt.show()
