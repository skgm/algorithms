"""
Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""

n = int(input('Введите количество элементов'))
ans = 0
num = 1
while n > 0:
    ans += num
    num /= -2
    n -= 1
print(f'Сумма {ans}')

# по аналогии вариант с рекурсией
# n = int(input('Введите количество элементов'))
# num = 1
# ans = 0
#
#
# def func(a):
#     global ans
#     global num
#     if a == 0:
#         return ans
#     ans += num
#     num /= -2
#     return func(a - 1)
#
#
# print(f'{func(n)}')
