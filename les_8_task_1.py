"""
Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
"""

import hashlib


def func(data):
    hash_string = set()
    value_string = set()
    for i in range(len(data)):
        for j in range(len(data), i, -1):
            hash_string.add(hashlib.sha1(data[i:j].encode('utf-8')).hexdigest())
            value_string.add(data[i:j])
            print(hash_string)
            print(data[i:j])
            print(value_string)
    value_string.remove(data)
    return f'Количество различных подстрок: {len(hash_string) - 1}, сами подстроки: {value_string}'


arr = 'sova'
print(func(arr))
