"""Animation of an evolving graph."""


class Control:
    """Hold graph and canvas, handle animation and updates."""

    def __init__(self, Model, View):
        self.model = Model()
        self.view = View()

    def update(self, *args):
        """Update graph and animation.
        Here modeling a Barabasi-Albert graph.
        """
        graph = self.model.update()
        self.view.draw(graph)

    def run(self):
        self.view.run(self.update)
