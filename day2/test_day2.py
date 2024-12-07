import pytest

from day2 import get_formatted_arr, find_safety_using_all


@pytest.fixture
def get_list_of_lists():
    out = get_formatted_arr('day2_test.txt')
    return out


def test_get_formatted_arr(get_list_of_lists):
    assert get_list_of_lists[0] == [7, 6, 4, 2, 1]


def test_main():
    assert find_safety_using_all('day2_test.txt') == 2
