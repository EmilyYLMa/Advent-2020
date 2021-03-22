import pytest
from two import (
    is_valid_password_1,
    is_valid_password_2,
    ParseError
)


@pytest.mark.parametrize('entry,expected_result', [
   ('2-3 x: xxrk', True),  # test correct if equal to min for lowercase
   ('2-3 X: XXrK', True),  # test correct if equal to min for uppercase
   ('2-3 x: xxrxk', True),  # test correct if equal to max
   ('2-3 x: xrk', False),  # test does not respect min
   ('2-3 x: xxxxxrk', False),  # test does not respect max
])
def test_check_password_1(entry, expected_result):
    res = is_valid_password_1(entry)
    assert res == expected_result


@pytest.mark.parametrize('entry,expected_result', [
   ('1-3 a: abcde', True),
   ('1-3 A: ABCDE', True),
   ('1-3 b: cdefg', False),
   ('2-9 c: cccccccccc', False),
])
def test_check_password_2(entry, expected_result):
    res = is_valid_password_2(entry)
    assert res == expected_result


@pytest.mark.parametrize('entry', [
    ('asd1-3 a: asdsa'),  # entry should start with a number
    ('1-3 av: asdsa'),  # there should only be one target character
    ('1-3a : sadsan'),  # space should exist between the number and target char
    ('1-3 a sdassad'),  # semi-colon shoudl exist between char and password
    ('1-3 a: 123'),  # password should be a letter
    ('1-3 1: abcse'),  # target character should be a letter
])
def test_bad_entry_is_reported_as_false(entry):
    with pytest.raises(ParseError):
        is_valid_password_1(entry)

    with pytest.raises(ParseError):
        is_valid_password_2(entry)
