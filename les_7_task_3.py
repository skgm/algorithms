"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.
"""

import random

MIN_ITEM = -100
MAX_ITEM = 100
m = int(input('Введите натуральное число'))
SIZE = 2 * m + 1

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)


def find_med(data):
    for i in range(len(data)):
        not_more = []
        not_less = []
        for j in range(len(data)):
            if i == j:
                continue
            elif data[i] >= data[j]:
                not_less.append(data[j])
            elif data[i] <= data[j]:
                not_more.append(data[j])
        if len(not_more) == len(not_less):
            return data[i]

print(f'медиана = {find_med(array)}')
array.sort()
print(array)
print(f'Проверка, что медиана находится по центру')