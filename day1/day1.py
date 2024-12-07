from collections import Counter

from typing import List


def find_sum_of_differences(file_path: str):
    two_lists = zip_up_the_two_lists(file_path)
    left, right = sort_lists(two_lists)
    sum_of_differences = 0
    for i in range(len(left)):
        sum_of_differences += abs(left[i] - right[i])
    return sum_of_differences


def zip_up_the_two_lists(file_path: str):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            split_line = line.split('   ')
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))
    return [left, right]


def sort_lists(lists: List[List[int]]):
    return [sorted(l) for l in lists]


def return_frequency_score(file_path: str):
    two_lists = zip_up_the_two_lists(file_path)
    left, right = two_lists[0], two_lists[1]
    frequency_score = 0
    right_counter = Counter(right)
    for num in left:
        frequency_score += num * right_counter.get(num, 0)
    return frequency_score


if __name__ == '__main__':
    print(find_sum_of_differences('day1/day1_input.txt'))
    print(return_frequency_score('day1/day1_input.txt'))
