def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_lower_list = [char.lower() for char in first_string]
    second_lower_list = [char.lower() for char in second_string]
    merge_sort(first_lower_list)
    merge_sort(second_lower_list)

    first_sorted = "".join(first_lower_list)
    second_sorted = "".join(second_lower_list)

    if (
        first_sorted != second_sorted
        or len(first_string) == 0
        or len(second_string) == 0
    ):
        return (first_sorted, second_sorted, False)
    else:
        return (first_sorted, second_sorted, True)
