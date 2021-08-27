from settings import *
from cell import Cell


class Grid:
    def __init__(self):
        # * create grid with settings
        self.grid = [[Cell(x, y) for x in range(COLUMNS)] for y in range(ROWS)]


if __name__ == '__main__':
    g = Grid()
    for r in g.grid:
        print(r)
