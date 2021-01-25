"""
Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

big = 0
number = 0
while True:
    num = int(input('Введите любое число, для выхода нажмите "0"'))
    if num == 0:
        break
    summ = 0
    print(num)
    number = num
    while num != 0:
        a = num % 10
        summ += a
        num //= 10
    if summ > big:
        big = summ

if number != 0:
    print(f'У числа {number} самая большая сумма цифр {big}')
else:
    print('Игра закончилась не начавшись')