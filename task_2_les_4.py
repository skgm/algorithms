"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
"""

from timeit import timeit
from cProfile import run


def find_simple(num):
    if num < 168:
        n = num * 10
    elif num < 1680:
        n = num * 100
    else:
        n = num * 1000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    ss = [i for i in sieve if i != 0]
    return ss[num]


print(timeit('find_simple(1)', number=100, globals=globals()))             # 0.0022473000000000007
print(timeit('find_simple(10)', number=100, globals=globals()))            # 0.0294055
print(timeit('find_simple(100)', number=100, globals=globals()))          # 4.0728990000000005

run('find_simple(1)')
run('find_simple(10)')
run('find_simple(100)')


#       6 function calls in 0.038 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.038    0.038 <string>:1(<module>)
#      1    0.032    0.032    0.037    0.037 task_2_les_4.py:14(find_simple)
#      1    0.003    0.003    0.003    0.003 task_2_les_4.py:21(<listcomp>)
#      1    0.002    0.002    0.002    0.002 task_2_les_4.py:29(<listcomp>)
#      1    0.000    0.000    0.038    0.038 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def test(num):
    if num < 168:
        n = num * 10
    elif num < 1680:
        n = num * 100
    else:
        n = num * 1000
    lst = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst[num]



print(timeit('test(1)', number=100, globals=globals()))            # 0.0003604000000000003
print(timeit('test(10)', number=100, globals=globals()))           # 0.016784200000000006
print(timeit('test(100)', number=100, globals=globals()))          # 0.46883289999999994

run('test(1)')
run('test(10)')
run('test(100)')


#       172 function calls in 0.004 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1    0.004    0.004    0.004    0.004 task_2_les_4.py:55(test)
#      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#    168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Алгоритм со вложенным циклом имеет сложность O(n^2) и 
в данном случае работает медленне чем алгоритм решета
на более больших данных.
"""