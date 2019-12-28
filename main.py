#!/usr/bin/env python3
"""Executable for simulation launching.
Make executable with :
    # chmod +x main.py
Give package name as an argument :
    $ ./main.py barabasi
-a flag for animaton :
    $ ./main.py -a barabasi
"""

import importlib
import re
from control import Control


def main(*args):
    """Launch simulation from provided package name."""
    name = "barabasi"
    animate = False

    for arg in args[1:]:
        if arg == "-a":
            animate = True
        else:
            name = re.sub("[^a-zA-Z_]", "", arg)

    if importlib.util.find_spec(name) is None:
        raise ModuleNotFoundError(f"Package '{name}' wasn't found.")
    package = importlib.import_module(name)
    Control(package.Model, package.View).run(animate)


if __name__ == "__main__":
    import sys
    from timer import Clock

    main(*sys.argv)
    for name, (n, time) in Clock.report().items():
        print(f"{name} (x{n}): {time:.3f} s")
