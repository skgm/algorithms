"""
В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.
"""


import random
SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

minn = array[0]
maxx = array[0]

for i in array:
    if minn > i:
        minn = i
    if maxx < i:
        maxx = i
min_index = array.index(minn)
max_index = array.index(maxx)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'значения мин {minn} и мах {maxx}')
print(f'индексы мин {min_index} и мах {max_index}')
print(array)



