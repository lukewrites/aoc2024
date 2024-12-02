from typing import List


def find_sum_of_differences(file_path:str):
    two_lists = zip_up_the_two_lists(file_path)
    left, right = sort_lists(two_lists)
    sum_of_differences = 0
    for i in range(len(left)):
        sum_of_differences += abs(left[i] - right[i])
    return sum_of_differences

def zip_up_the_two_lists(file_path:str):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        left, right = [], []
        for line in lines:
            split_line = line.split('   ')
            left.append(int(split_line[0]))
            right.append(int(split_line[1]))
    return [left, right]

def sort_lists(lists:List[List[int]]):
    return [sorted(l) for l in lists]

if __name__ == '__main__':
    print(find_sum_of_differences('day1/day1_input.txt'))