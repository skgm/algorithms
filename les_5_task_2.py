"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
[‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
[‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


HEX_DICT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
            10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(x, y):
    result = deque()
    remainder = 0
    x = deque(x)
    y = deque(y)
    if len(y) > len(x):
        x, y = y, x

    while x:
        if y:
            res = HEX_DICT[x.pop()] + HEX_DICT[y.pop()] + remainder
        else:
            res = HEX_DICT[x.pop()] + remainder
        remainder = 0
        if res < 16:
            result.appendleft(HEX_DICT[res])
        else:
            result.appendleft(HEX_DICT[res - 16])
            remainder = 1
    if remainder:
        result.appendleft('1')

    return result


def mult_hex(x, y):
    x = deque(x)
    y = deque(y)
    if len(y) > len(x):
        x, y = y, x

    y.reverse()
    x.reverse()
    tmp = 0
    term = []

    for i in range(len(y)):
        res = 0
        interim = deque()

        if i > 0:
            for k in range(i):
                interim.appendleft(HEX_DICT[0])

        for j in range(len(x)):
            if tmp:
                num = HEX_DICT[y[i]] * HEX_DICT[x[j]] + tmp
            else:
                num = HEX_DICT[y[i]] * HEX_DICT[x[j]]
            if num < 16:
                    res = num
                    tmp = 0
            else:
                tmp = num // 16
                res = num - tmp * 16
            interim.appendleft(HEX_DICT[res])

        if tmp:
            interim.appendleft(HEX_DICT[tmp])
        term.append(interim)
        tmp = 0

    if len(term) < 2:
        return term[0]
    elif len(term) == 2:
        return sum_hex(term[0], term[1])
    else:
        result = deque()
        for i in term:
            result = sum_hex(result, i)
        return result


a = list(input('Введите 1-е шестнадцатиричное число: ').upper())
b = list(input('Введите 2-е шестнадцатиричное число: ').upper())


print(*a, '+', *b, '=', *sum_hex(a, b))
print(*a, '+', *b, '=', *mult_hex(a, b))





