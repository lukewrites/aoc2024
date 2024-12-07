def find_safety_using_all(file_path):
    arrs = get_formatted_arr(file_path)
    safe_count = 0
    for arr in arrs:
        if (all(arr[i] > arr[i - 1] and arr[i] - arr[i - 1] <= 3 for i in range(1, len(arr)))
                or all(arr[i] < arr[i - 1] and arr[i - 1] - arr[i] <= 3 for i in range(1, len(arr)))):
            safe_count += 1
    return safe_count


def get_formatted_arr(file_path):
    with open(file_path, 'r') as input_file:
        lines = input_file.readlines()
        work_arrays = []
        for line in lines:
            temp_line = list(map(int, line.split(' ')))
            work_arrays.append(temp_line)
    return work_arrays


if __name__ == '__main__':
    print(find_safety_using_all('day2_input.txt'))
