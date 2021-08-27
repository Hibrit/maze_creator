from settings import CELL_SIZE, COLUMNS, HEIGHT, LINE_TICKNESS, ROWS, WIDTH
from grid import Grid
from random import choice
from PIL import Image, ImageDraw


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

    for _ in range(ROWS * COLUMNS - 2):
        connection = choice(grid.get_all_possible_connections(connections))
        connections.append(connection)
        connection[1].connected = True

    # * create the maze image
    im = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 255))
    draw = ImageDraw.Draw(im)

    # * draw walls
    grid.reset_connections()
    # for row in grid.grid:
    #     print(row)

    for row in grid.grid:
        for cell in row:
            cell.connected = True
            neighbours = grid.get_neighbours(cell)
            to_draw = []
            # print(cell.x, cell.y)
            # print(neighbours)

            for n in neighbours:
                if (cell, n) in connections or (n, cell) in connections:
                    continue
                else:
                    to_draw.append((cell, n))

            for c1, c2 in to_draw:
                vertical = c1.y != c2.y
                if vertical:
                    sp = c1 if c1.y > c2.y else c2

                    starting_point = (sp.x * CELL_SIZE, sp.y * CELL_SIZE)

                    shape = [starting_point,
                             (starting_point[0] + CELL_SIZE, starting_point[1])]

                else:
                    sp = c1 if c1.x > c2.x else c2

                    starting_point = (sp.x * CELL_SIZE, sp.y * CELL_SIZE)

                    shape = [starting_point,
                             (starting_point[0], starting_point[1] + CELL_SIZE)]

                draw.line(shape, fill="#000000", width=LINE_TICKNESS)

    im.show()


if __name__ == '__main__':
    main()
