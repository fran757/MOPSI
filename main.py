from model import Barabasi
from view import View
from control import Control

if __name__ == "__main__":
    Control(Barabasi, View).run()
