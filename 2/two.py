import argparse
import re


class ParseError(Exception):
    pass


def is_valid_entry(entry):
    # entry must have the format: Number-Number Letter: String of Letters
    pattern = re.compile(r'^\d+-\d+\s[A-Za-z]{1}\:\s+[A-Za-z]')

    return True if re.search(pattern, entry) else False


def parse_entry(entry):
    if is_valid_entry(entry):
        policy, password = entry.split(':')
        count, char = policy.split()
        num_1, num_2 = count.split('-')
    else:
        raise ParseError(f"Unable to parse entry: {entry}")

    return (num_1, num_2, char, password)


def is_valid_password_1(entry):
    try:
        min_count, max_count, char, password = parse_entry(entry)
    except ParseError as e:
        raise e

    return int(min_count) <= password.count(char) <= int(max_count)


def is_valid_password_2(entry):
    try:
        index_1, index_2, char, password = parse_entry(entry)
        password = password.replace(" ", '')
        char_set = set([
            password[int(index_1)-1],
            password[int(index_2)-1]
        ])
    except ParseError as e:
        raise e

    return char in char_set and len(char_set) == 2


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--filename',
        required=True,
        help='Filename of input data.'
    )
    args = parser.parse_args()

    total_valid_passwords_1 = 0
    total_valid_passwords_2 = 0

    with open(args.filename) as f:
        for entry in f:
            try:
                if is_valid_password_1(entry):
                    total_valid_passwords_1 += 1
            except ParseError as e:
                print(e)

            try:
                if is_valid_password_2(entry):
                    total_valid_passwords_2 += 1
            except ParseError as e:
                print(e)

    print(f'Total Valid Passwords - Part 1: {total_valid_passwords_1}')
    print(f'Total Valid Passwords - Part 2: {total_valid_passwords_2}')
