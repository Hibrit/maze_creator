from grid import Grid
from random import choice, seed

seed(1)


def main():
    # * create grid
    grid = Grid()
    connections = []
    # * initialize first connection
    starting_cell = grid.choose_random_cell()
    first_connected_cell = choice(grid.get_neighbours(starting_cell))
    connections.append((starting_cell, first_connected_cell))
    # * mark first connection as connected
    starting_cell.connected = True
    first_connected_cell.connected = True

    print(connections)
    # for r in grid.grid:
    #     print(r)
    # print(starting_cell)
    # print(choice(grid.get_neighbours(starting_cell)))
    # connections.append([starting_cell])


if __name__ == '__main__':
    main()
