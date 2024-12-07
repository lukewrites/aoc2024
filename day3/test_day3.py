from day3 import find_all_mul_operators, read_input, the_big_multiplier


def test_the_big_multiplier():
    test_input = read_input('day3_test.txt')
    muls = find_all_mul_operators(test_input)
    output = the_big_multiplier(muls)
    assert output == 161
