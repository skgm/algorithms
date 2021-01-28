"""
Определить, какое число в массиве встречается чаще всего.
"""

import random
SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

arr_set = set(array)
print(arr_set)
d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
mx = 0
amount = 0
for i, j in d.items():
    if mx < i:
        mx = i
        amount = j
print(f'Число {mx} появляляется {amount} раз ')
