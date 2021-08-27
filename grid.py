import random
from settings import *
from cell import Cell
from random import choice


class Grid:
    def __init__(self):
        # * create grid with settings
        self.grid = [[Cell(x, y) for x in range(COLUMNS)] for y in range(ROWS)]

    def choose_random_cell(self) -> Cell:
        return choice(choice(self.grid))

    def get_neighbours(self, cell: Cell) -> list[Cell]:
        x = cell.x
        y = cell.y
        possible_neighbours = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
        neighbours = []

        for n in possible_neighbours:
            if n[0] < 0 or n[1] < 0:
                continue

            try:
                current_cell = self.grid[n[1]][n[0]]
                if not current_cell.connected:
                    neighbours.append(current_cell)
            except IndexError:
                pass

        return neighbours

    def get_all_neighbours(self, connections):
        pass


if __name__ == '__main__':
    g = Grid()
    random_cell = g.choose_random_cell()
    neighbours = g.get_neighbours(random_cell)
    for r in g.grid:
        print(r)
    print(random_cell)
    print(neighbours)
