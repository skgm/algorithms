"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random
from timeit import timeit
from cProfile import run

SIZE = 10
BIG_SIZE = 100
MIN_ITEM = -100
MAX_ITEM = 100


# Ускоренная сортировка
def bubble_sort(data):
    mark = True
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                mark = False
        if mark is True:
            break
        # print(data)
    return data


# Обычный пузырек
def default_func(data):
    n = 1
    while n < len(data):
        for i in range(len(data)-n):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
        # print(data)
    return data


test1 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
test2 = [random.randint(MIN_ITEM, MAX_ITEM) for j in range(BIG_SIZE)]
test3 = [random.randint(MIN_ITEM, MAX_ITEM) for n in range(SIZE)]
test4 = [random.randint(MIN_ITEM, MAX_ITEM) for m in range(BIG_SIZE)]
ideal_test1 = [k for k in range(BIG_SIZE - 1, -1, -1)]
ideal_test2 = [k for k in range(BIG_SIZE - 1, -1, -1)]

print(id(ideal_test1))
print(id(ideal_test2))


print(f'Массив : \n{test1}')
print(f'Отсоритрованный в обратном порядке массив: \n{bubble_sort(test1)}')

res_test1 = timeit('bubble_sort(test1)', number=100, globals=globals())
res_test2 = timeit('bubble_sort(test2)', number=100, globals=globals())
res_test3 = timeit('default_func(test3)', number=100, globals=globals())
res_test4 = timeit('default_func(test4)', number=100, globals=globals())
res_test5 = timeit('bubble_sort(ideal_test1)', number=100, globals=globals())
res_test6 = timeit('default_func(ideal_test2)', number=100, globals=globals())
print(f'Время ускоренной функции с 10 элементами: \t{res_test1}\n'
      f'Время ускоренной функции с 100 элементами: \t{res_test2}\n'
      f'Время обычной функции с 10 элементами: \t\t{res_test3}\n'
      f'Время обычной функции с 100 элементами: \t{res_test4}\n')
print(res_test5)
print(res_test6)

