"""Visual representation of a graph."""

import view


class View(view.View):
    """Anthill-specific graph representation."""

    def draw(self, model):
        """Highlight special nodes and reinforced paths."""
        graph = model.graph
        ants = model.ants
        sugar = model.sugar
        nest = model.nest

        colors = ["w"] * len(graph.nodes)
        colors[nest] = "b"
        colors[sugar] = "r"
        for ant in ants:
            colors[ant.position] = "k"

        weights = [graph[u][v]["weight"] / 5 for u, v in graph.edges()]
        super().draw(graph, node_color=colors, width=weights)#, arrows=True)
