"""Animation of an evolving graph."""
from timer import clock


class Control:
    """Hold graph and canvas, handle animation and updates."""

    def __init__(self, Model, View):
        self.model = Model()
        self.view = View()

    def run(self, animate=False):
        """Start simulation."""
        if animate:

            def update(*args):
                clock(self.model.update)()
                clock(self.view.draw)(self.model)

            self.view.run(update)
        else:
            for _ in range(1000):
                clock(self.model.update)()
            clock(self.view.draw)(self.model)
            self.view.show()
