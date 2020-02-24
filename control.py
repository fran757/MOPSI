"""Animation of an evolving graph."""
import numpy as np
import math

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
            for _ in range(10):
                model = self.model
                for _ in range(1000):
                    clock(self.model.update)()
                clock(self.view.draw)(self.model)
                self.view.show()

            return

            import matplotlib.pyplot as plt
            graph = self.model.graph
            degrees = [len(adj[1]) for adj in graph.adjacency()]
            D = [d + 1 for d in range(max(degrees))]

            N = np.zeros_like(D)
            for d in degrees:
                N[d - 1] += 1

            tN = [len(degrees) / (d*(d+1)*(d+2)) for d in D]
            def log_scale(X, Y):
                lX, lY = [], []
                for d, n in zip(X, Y):
                    try:
                        ld, ln = math.log(d), math.log(n)
                        lX.append(ld)
                        lY.append(ln)
                    except ValueError:
                        pass
                return lX, lY

            n = len(degrees) - 1
            plt.title(f"log scale degree repartition after {n} steps")
            plt.plot(*log_scale(D, N), "b.", label="empirical")
            plt.plot(*log_scale(D, tN), "r-", label="theorical")
            plt.xlabel("$\log(d)$")
            plt.ylabel("$\log(N(d))$")
            plt.legend()
            plt.hlines([0], 0, math.log(max(D)))
            plt.show()
