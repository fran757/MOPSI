"""Visual representation of a graph."""

import view


class View(view.View):
    """Barabasi graph representation."""

    def draw(self, model):
        """Highlight degree variations."""
        graph = model.graph
        degrees = [len(adj[1]) for adj in graph.adjacency()]
        super().draw(graph, node_color=degrees)
