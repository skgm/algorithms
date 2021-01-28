"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


a = {i for i in range(2, 100)}
b = {i for i in range(2, 10)}
d = {i: 0 for i in range(2, 10)}

for i in a:
    for j in b:
        if i % j == 0:
            d[j] += 1

print(d)
