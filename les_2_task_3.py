"""
Сформировать из введенного числа обратное
по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""

x = int(input('Введите натуральное число\n'))
digit = 0


def func(a):
    global digit
    if a == 0:
        return digit
    num = a % 10
    digit *= 10
    digit += num
    return func(a // 10)


print(f'Обратное по порядку{func(x)}')




