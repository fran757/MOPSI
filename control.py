"""Animation of an evolving graph."""
from timer import clock


class Control:
    """Hold graph and canvas, handle animation and updates."""

    def __init__(self, Model, View, animate=False):
        self.model = Model()
        self.view = View()
        self.animate = animate

    @clock
    def update(self, *args):
        """Update graph and animation.
        Here modeling a Barabasi-Albert graph.
        """
        self.model.update()

    @clock
    def run(self):
        """Start simulation."""
        if self.animate:
            def update(*args):
                self.update()
                self.view.draw(self.model)
            self.view.run(update)

        for _ in range(500):
            self.update()
        self.view.draw(self.model)
        self.view.show()
