import argparse


class NoEntriesFound(Exception):
    pass


def find_two_entries(data, target_number):
    for x in data:
        y = target_number - x
        if y in data:
            return x, y, x * y
    else:
        raise NoEntriesFound(
            f'There are no two entries that add up to {target_number}'
        )


def find_three_entries(data, target_number):
    for x in data:
        for y in data:
            z = target_number - x - y
            if z in data:
                return x, y, z, x * y * z
    else:
        raise NoEntriesFound(
            f'There are no three entries that add up to {target_number}.'
        )


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filename',
        required=True,
        help='Filename of input data.'
    )
    args = parser.parse_args()

    with open(args.filename) as f:
        data = [float(x) for x in f]

    try:
        x, y, z = find_two_entries(data, 2020)
        print(f'Product of the Two Entries that Add Up to 2020: {z}.')
    except NoEntriesFound as e:
        print(e)

    try:
        x, y, z, w = find_three_entries(data, 2020)
        print(f'Product of the Three Entries that Add Up to 2020: {w}.')
    except NoEntriesFound as e:
        print(e)
