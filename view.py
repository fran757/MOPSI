"""Basic visual representation of a graph."""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as ani

from timer import clock


class View:
    """Spring layout graph representation."""
    spring=True

    def __init__(self):
        self.figure, self.axis = plt.subplots()
        self.positions = {}
        self.old_nodes = []

    @clock
    def draw(self, graph, **kwargs):
        """Draw updated graph, holding old nodes into place."""
        if self.spring:
            hold = {}
            if self.positions:
                hold.update(pos=self.positions, fixed=self.old_nodes)
            if not self.positions or len(self.old_nodes) != len(graph.nodes):
                self.positions = nx.spring_layout(graph, **hold)
            self.old_nodes = list(graph.nodes)
        else:
            self.positions = {node: node for node in graph.nodes}

        self.axis.clear()
        cmap = plt.cm.viridis
        if not all(key in ["node_color", "width", "arrows"] for key in kwargs):
            raise KeyError("Wrong keyword arguments : " + ", ".join(kwargs))
        # if "node_color" in kwargs:
        #     colors = kwargs["node_color"]
        #     cb = plt.colorbar(plt.cm.ScalarMappable(plt.Normalize(min(colors), max(colors), cmap)), ax=self.axis)

        #     cb.ax.set_ylabel("node degree")
        # plt.title("Anthill path finding on grid with obstacle")

        n = len(graph.nodes)
        nx.draw(graph, ax=self.axis, pos=self.positions, node_size=20, cmap=cmap, **kwargs)

    def run(self, update):
        """Run animation of given function."""
        anim = ani.FuncAnimation(self.figure, update, interval=0)
        self.show()

    def show(self):
        plt.show()
