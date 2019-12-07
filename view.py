"""Basic visual representation of a graph."""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani


class View:
    """Spring layout graph representation."""

    def __init__(self):
        self.figure, self.axis = plt.subplots()
        self.positions = {}
        self.old_nodes = []

    def draw(self, graph, **kwargs):
        """Draw updated graph, holding old nodes into place."""
        hold = {}
        if self.positions:
            hold.update(pos=self.positions, fixed=self.old_nodes)
        if not self.positions or len(self.old_nodes) != len(graph.nodes):
            self.positions = nx.spring_layout(graph, **hold)
        self.old_nodes = list(graph.nodes)

        self.axis.clear()
        if not all(key in ["node_color", "width", "arrows"] for key in kwargs):
            raise KeyError("Wrong keyword arguments : " + ", ".join(kwargs))
        nx.draw(graph, ax=self.axis, pos=self.positions, node_size=30, **kwargs)

    def run(self, update):
        """Run animation of given function."""
        anim = ani.FuncAnimation(self.figure, update, interval=10)
        plt.show()
