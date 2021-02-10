"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49

array = [random.uniform(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)


def merge_sort(data):
    if len(data) <= 1:
        return data

    pivot = len(data) // 2
    left = merge_sort(data[:pivot])
    right = merge_sort(data[pivot:])

    left_index, right_index = 0, 0
    new_array = []
    common_len = len(left) + len(right)

    for i in range(common_len):
        if len(right) > right_index and len(left) > left_index:
            if left[left_index] <= right[right_index]:
                new_array.append(left[left_index])
                left_index += 1
            else:
                new_array.append(right[right_index])
                right_index += 1

    new_array += left[left_index:]
    new_array += right[right_index:]
    return new_array
        

print(f'Отсортированный массив: \n{merge_sort(array)}')

