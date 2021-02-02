"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.

Задача:
Определить, какое число в массиве встречается чаще всего.
"""

from timeit import timeit
from random import randint
from cProfile import run

min_item = 0
max_item = 100


def frequent_number_two_cycles(n):
    array = [randint(min_item, max_item) for i in range(n)]
    d = {}
    for i in array:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    mx = 0
    amount = 1
    for i, j in d.items():
        if amount < j:
            mx = i
            amount = j


print(timeit('frequent_number_two_cycles(10)', number=100, globals=globals()))          # 0.002217399999999998
print(timeit('frequent_number_two_cycles(100)', number=100, globals=globals()))         # 0.018702999999999997
print(timeit('frequent_number_two_cycles(1_000)', number=100, globals=globals()))       # 0.1184732
print(timeit('frequent_number_two_cycles(10_000)', number=100, globals=globals()))      # 1.0335874
print(timeit('frequent_number_two_cycles(100_000)', number=100, globals=globals()))     # 12.1792482


run('frequent_number_two_cycles(10)')
run('frequent_number_two_cycles(100)')
run('frequent_number_two_cycles(1_000)')
run('frequent_number_two_cycles(10_000)')
run('frequent_number_two_cycles(100_000)')


   #       526911 function calls in 0.202 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.202    0.202 <string>:1(<module>)
   # 100000    0.058    0.000    0.130    0.000 random.py:200(randrange)
   # 100000    0.034    0.000    0.164    0.000 random.py:244(randint)
   # 100000    0.048    0.000    0.072    0.000 random.py:250(_randbelow_with_getrandbits)
   #      1    0.011    0.011    0.202    0.202 task_1_les_4.py:47(frequent_number_two_cycles)
   #      1    0.027    0.027    0.191    0.191 task_1_les_4.py:48(<listcomp>)
   #      1    0.000    0.000    0.202    0.202 {built-in method builtins.exec}
   # 100000    0.010    0.000    0.010    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   # 126905    0.014    0.000    0.014    0.000 {method 'getrandbits' of '_random.Random' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


def frequent_number_cycle_in_cycle(n):
    array = [randint(min_item, max_item) for i in range(n)]
    max_amount = 1
    num = array[0]
    for i in range(len(array)):
        amount = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                amount += 1
        if max_amount < amount:
            max_amount = amount
            num = array[i]


print(timeit('frequent_number_cycle_in_cycle(10)', number=100, globals=globals()))          # 0.003295199999999998
print(timeit('frequent_number_cycle_in_cycle(100)', number=100, globals=globals()))         # 0.0644913
print(timeit('frequent_number_cycle_in_cycle(1_000)', number=100, globals=globals()))       # 6.855808700000001


run('frequent_number_cycle_in_cycle(10)')
run('frequent_number_cycle_in_cycle(100)')
run('frequent_number_cycle_in_cycle(1_000)')


   #       6258 function calls in 0.062 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.062    0.062 <string>:1(<module>)
   #   1000    0.001    0.000    0.001    0.000 random.py:200(randrange)
   #   1000    0.000    0.000    0.002    0.000 random.py:244(randint)
   #   1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
   #      1    0.060    0.060    0.062    0.062 task_1_les_4.py:97(frequent_number_cycle_in_cycle)
   #      1    0.000    0.000    0.002    0.002 task_1_les_4.py:98(<listcomp>)
   #      1    0.000    0.000    0.062    0.062 {built-in method builtins.exec}
   #   1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #   1252    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


def frequent_number_with_count(n):
    array = [randint(min_item, max_item) for i in range(n)]
    num = array[0]
    amount = array.count(num)
    for i in array:
        if array.count(i) > amount:
            amount = array.count(i)
            num = i


print(timeit('frequent_number_with_count(10)', number=100, globals=globals()))          # 0.0013108000000000009
print(timeit('frequent_number_with_count(100)', number=100, globals=globals()))         # 0.029709100000000002
print(timeit('frequent_number_with_count(1_000)', number=100, globals=globals()))       # 1.8307116
print(timeit('frequent_number_with_count(10_000)', number=100, globals=globals()))      # 162.99653610000001


run('frequent_number_with_count(10)')
run('frequent_number_with_count(100)')
run('frequent_number_with_count(1_000)')
run('frequent_number_with_count(10_000)')


   #       62612 function calls in 1.654 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    1.654    1.654 <string>:1(<module>)
   #  10000    0.006    0.000    0.013    0.000 random.py:200(randrange)
   #  10000    0.003    0.000    0.017    0.000 random.py:244(randint)
   #  10000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
   #      1    0.003    0.003    1.654    1.654 task_1_les_4.py:149(frequent_number_with_count)
   #      1    0.003    0.003    0.019    0.019 task_1_les_4.py:150(<listcomp>)
   #      1    0.000    0.000    1.654    1.654 {built-in method builtins.exec}
   #  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
   #  10002    1.632    0.000    1.632    0.000 {method 'count' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #  12605    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}


"""
Первый алгоритм имеет линейный вид, асимптотическая сложность O(n) (константу 2 можно убрать)
Второй алгоритм имеет квадратичный вид, асимптотичкая сложность О(n^2)
Третий алгоритм при больших данных имеет слабое место в виде метода списка count()
Из этого следует, что первый вариант самый оптимальный среди 3-х алгоритмов.
При больших данных он быстрее справляется с задачей.
"""
