"""
Вводятся три разных числа.
Найти, какое из них является средним
(больше одного, но меньше другого).
"""

first = int(input('Введите первое число'))
second = int(input('Введите второе число'))
third = int(input('Введите третье число'))

if first < second < third or third < second < first:
    print(f'Среднее число: {second}')
elif second < first < third or third < first < second:
    print(f'Среднее число: {first}')
else:
    print(f'Среднее число: {third}')