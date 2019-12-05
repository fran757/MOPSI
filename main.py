#!/usr/bin/env python3

from control import Control
from importlib import import_module
import sys


if __name__ == "__main__":
    try:
        name = sys.argv[1]
    except IndexError:
        name = "barabasi"

    try:
        package = import_module(name)
        Control(package.Model, package.View).run()
    except ModuleNotFoundError:
        print(f"No module found with name '{name}'.")
