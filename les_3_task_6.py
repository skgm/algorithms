"""
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random
SIZE = 10
MIN_ITEM = -100
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

print(f'Минимальный элемент {minn} находится под {min_index}-м индексом\n'
      f'Максимальный элемент {maxx} находится под {max_index}-м индексом')
if max_index < min_index:
    cp = array[max_index + 1: min_index]
else:
    cp = array[min_index + 1: max_index]
print(cp)
summ = 0
if cp:
    for i in cp:
        summ += i
    print(f'Сумма равна {summ}')
else:
    print('Список пуст')
