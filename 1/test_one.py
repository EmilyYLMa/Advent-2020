import pytest
from one import (
    find_two_entries,
    find_three_entries,
    NoEntriesFound
)


@pytest.mark.parametrize("data,target_number", [
    ([1, 2, 4, 5, 8], 10),
    ([1, -2, 4, 5, 8], -1),  # test negative target number
    ([1.5, 2, 4, 5.5, 8], 7),  # test entries can be floats
])
def test_find_two_entries(data, target_number):
    x, y, z = find_two_entries(data, target_number)

    assert x + y == target_number
    assert z == x*y


@pytest.mark.parametrize('data,target_number', [
    ([1, 2, 4, 5, 8], 100),
    ([], 100),
])
def test_no_two_entries_add_to_target(data, target_number):
    with pytest.raises(NoEntriesFound):
        find_two_entries(data, target_number)


@pytest.mark.parametrize("data,target_number", [
    ([1, 2, 3, 4, 5], 6),
    ([1, 2, -3, 4, 5], -2),  # test negative target number
    ([1.5, 2, 4, 5.5, 8], 9),  # test entries can be floats
])
def test_find_three_entries(data, target_number):
    x, y, z, w = find_three_entries(data, target_number)

    assert x + y + z == target_number
    assert w == x * y * z


@pytest.mark.parametrize('data,target_number', [
    ([1, 2, 3, 4, 5], 100),
    ([], 100),
])
def test_no_three_entries_add_to_target(data, target_number):
    with pytest.raises(NoEntriesFound):
        find_three_entries(data, target_number)
