"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

x = int(input('Введите натуральное число'))
even = 0
odd = 0


def func(a):
    global even
    global odd
    if a == 0:
        return f'В числе {x} {even} четных и {odd} нечетных цифр'
    s = a % 10
    if s % 2 == 0:
        print(f'Цифра {s} - четная')
        even += 1
    else:
        print(f'Цифра {s} - нечетная')
        odd += 1
    a = int(a / 10)
    return f'{func(a)}'


print(func(x))
