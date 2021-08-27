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

    while True:
        connection = choice(grid.get_all_possible_connections(connections))
        connections.append(connection)
        connection[1].connected = True
        break

    for r in grid.grid:
        print(r)
    print(connections)
    print(grid.get_all_possible_connections(connections))


if __name__ == '__main__':
    main()
