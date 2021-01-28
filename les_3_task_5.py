"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

b = -10000000000000
inx = 0
for i, item in enumerate(array):
    if item < 0 and item > b:
        b = item
        inx = i

print(f'Максимальный отрицательный элемент {b} имеет индекс {inx}')

