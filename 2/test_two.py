import pytest
from two import (
    is_valid_password_1,
    is_valid_password_2,
    ParseError
)


@pytest.mark.parametrize('entry,expected_result', [
   ('2-3 x: xxrk', True),  # test lower-case target count equal to min
   ('2-3 X: XXrK', True),  # test upper-case target count equal to min
   ('2-3 x: xxrxk', True),  # test target count equal to max
   ('2-4 x: xxxrxk', True),  # test target count in between min or max
   ('2-3 x: xrk', False),  # test does not respect min
   ('2-3 x: xxxxxrk', False),  # test does not respect max
])
def test_check_password_1(entry, expected_result):
    res = is_valid_password_1(entry)
    assert res == expected_result


@pytest.mark.parametrize('entry,expected_result', [
   ('1-3 a: abcde', True),  # test lower-case target on index 1
   ('1-3 A: ABCDE', True),  # test upper-case target on index 1
   ('1-3 A: BBADE', True),  # test upper-case target on index 2
   ('1-3 b: cdefg', False),  # test target not on index 1 or index 2
   ('2-9 c: cccccccccc', False),  # test target on index 1 and index 2
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
