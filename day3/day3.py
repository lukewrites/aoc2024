import re


def read_input(file_name):
    with open(file_name, 'r') as f:
        return f.read()


def find_all_mul_operators(expression):
    return re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', expression)


def the_big_multiplier(list_of_matches: list[list[str]]) -> int:
    total = 0
    for match in list_of_matches:
        total += int(match[0]) * int(match[1])
    return total


if __name__ == '__main__':
    text_in = read_input('day3_input.txt')
    matches = find_all_mul_operators(text_in)
    print(the_big_multiplier(matches))
