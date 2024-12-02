from day1 import find_sum_of_differences, zip_up_the_two_lists, sort_lists


def test_zip_up_the_two_lists_returns_correct_lists():
    two_lists = zip_up_the_two_lists('day1/day_test_input.txt')
    assert two_lists[0] == [3, 4, 2, 1, 3, 3]
    assert two_lists[1] == [4, 3, 5, 3, 9, 3]

def test_sort_lists():
    assert sort_lists([[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]]) == [[1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]]

def test_find_sum_of_differences():
    assert find_sum_of_differences('day1/day_test_input.txt') == 11