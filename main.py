#!/usr/bin/env python3
"""Executable for simulation launching.
Make executable with :
    # chmod +x main.py
Give package name as arguments :
    $ ./main.py barabasi
"""

from control import Control
from importlib import import_module


def main(*args):
    """Launch simulation from provided package name."""
    try:
        name = args[1]
    except IndexError:
        name = "barabasi"

    try:
        package = import_module(name)
        Control(package.Model, package.View).run()
    except ModuleNotFoundError:
        print(f"No module found with name '{name}'.")


if __name__ == "__main__":
    import sys
    main(*sys.argv)
