import argparse
import numpy


def find_number_trees(grid, route):
    # if empty grid, return 0 trees found
    if not grid:
        return 0

    parsed_grid = grid.splitlines()
    len_x, len_y = len(parsed_grid[0]), len(parsed_grid)

    x_route, y_route = route
    x, y = (0, 0)  # starting location

    num_trees = 0

    # while we're not at the bottom of the map
    while y < len_y - 1:

        # check if we need to refresh the x coordinates
        if (x + x_route) > (len_x - 1):
            x_update = (x + x_route) % len_x
            x = x_update
        else:
            x = x + x_route

        y = y + y_route

        if parsed_grid[y][x] == '#':
            num_trees += 1

    return num_trees


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filename',
        required=True,
        help='Filename of input data.'
    )
    args = parser.parse_args()

    with open(args.filename) as f:
        grid = f.read()

        # Part 1
        num_trees = find_number_trees(grid, (3, 1))
        print(f'Number Of Trees With Slope (3,1): {num_trees}')

        # Part 2
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        res = numpy.prod([find_number_trees(grid, s) for s in slopes])
        print(f'Multiplied Number of Trees: {res}')
