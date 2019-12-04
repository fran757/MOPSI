"""Animation of Barabasi-Albert graph construction."""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani


class Simulation:
    """Hold graph and canvas, handle animation and updates.
    Obviously should be separated into MVC later.
    """

    def __init__(self):
        self.figure, self.axis = plt.subplots()
        self.graph = nx.Graph([[0, 0]])
        self.positions = nx.spring_layout(self.graph)

    def update(self, *args):
        """Update graph and animation."""
        self.axis.clear()
        old_nodes = list(self.graph.nodes)

        degrees = np.array([len(adj[1]) for adj in self.graph.adjacency()])
        n = self.graph.number_of_nodes()
        connect = np.random.choice(n, p=degrees / sum(degrees))
        self.graph.add_edge(connect, n)

        degrees = np.array([len(adj[1]) for adj in self.graph.adjacency()])
        self.positions = nx.spring_layout(self.graph, pos=self.positions, fixed=old_nodes)
        nx.draw(
            self.graph,
            pos=self.positions,
            ax=self.axis,
            node_color=degrees,
            node_size=50,
            cmap=plt.cm.bwr,
        )

    def run(self):
        """Run simulation."""
        anim = ani.FuncAnimation(self.figure, self.update, interval=50)
        plt.show()


if __name__ == "__main__":
    Simulation().run()
