import pytest

from three import find_number_trees


test_string = test_string = \
'''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
'''


@pytest.mark.parametrize('slope,num_trees', [
    ((1, 1), 2),
    ((3, 1), 7),
    ((5, 1), 3),
    ((7, 1), 4),
    ((1, 2), 2),
])
def test_find_number_trees(slope, num_trees):
    res = find_number_trees(test_string, slope)
    assert res == num_trees


def test_empty_string():
    res = find_number_trees('', (3, 1))
    assert res == 0
