from import_defaults import *


class Colors:
    # random assignment of colors to tetromines
    colors = ["limegreen", "red", "blue", "yellow", "purple", "orange", "cyan"]

    @staticmethod
    def color():
        return Colors.colors[random.randrange(0, len(Colors.colors))]
