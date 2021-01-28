"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

arr = []
minn = array[0]
minn_2 = array[1]
for i in array:
    if minn > i:
        minn_2 = minn
        minn = i
    elif minn_2 > i:
        minn_2 = i

print(f'Два наименьших элемента: {minn} и {minn_2}')
