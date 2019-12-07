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
        self.model.update()
        self.view.draw(self.model)

    def run(self):
        """Start simulation."""
        self.view.run(self.update)
