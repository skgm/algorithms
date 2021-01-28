"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

N = 5
M = 4
MAX_SIZE = 5
MIN_SIZE = 0
array = [[random.randint(MIN_SIZE, MAX_SIZE)for j in range(M)]for i in range(N)]
print('\n'.join([''.join(['%s\t' % i for i in row]) for row in array]))

mx = MIN_SIZE - 1

arr = []
for j in range(M):
    tmp = []
    for i in range(N):
        tmp += [array[i][j]]
    arr += [tmp]

for i in range(M):
    mn = MAX_SIZE + 1
    for j in range(N):
        ix_j = 0
        if arr[i][j] < mn:
            mn = arr[i][j]
    if mx < mn:
        mx = mn

print(f'Максимум {mx}')
