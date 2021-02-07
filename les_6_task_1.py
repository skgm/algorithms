"""
Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
-------------------------------------------------------------------------------------------------
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random
from sys import getsizeof
from collections import deque

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100


array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(array)

# Вариант 1
minn = array[0]
minn_2 = array[1]
for i in array:
    if minn > i:
        minn_2 = minn
        minn = i
    elif minn_2 > i:
        minn_2 = i

print(f'Два наименьших элемента: {minn} и {minn_2}')
first_test = [SIZE, MIN_ITEM, MAX_ITEM, array, minn, minn_2]

# Вариант 2
sec_array = deque(random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE))
sorted_array = deque(sorted(sec_array))
first = sorted_array[0]
second = sorted_array[1]
print(f'Два наименьших элемента: {first} и {second}')


second_test = [SIZE, MIN_ITEM, MAX_ITEM, sec_array, sorted_array, first, second]


# Вариант 3
third_array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
third_array.sort()
fst = third_array[0]
scd = third_array[1]
print(f'Два наименьших элемента: {fst} и {scd}')


third_test = [SIZE, MIN_ITEM, MAX_ITEM, third_array, fst, scd]


def memory_size(object):
    print(object)
    # print(f'Объект {object=}\t {type(object)=}\t {getsizeof(object)=}\n')
    memory = 0
    # Расчитывается, что в аргумент функции будет подаваться список со всеми исползуемыми переменными и структурами
    for i in object:
        if hasattr(i, '__iter__'):
            if hasattr(i, 'items'):
                memory += getsizeof(i)
                for key, value in i.items():
                    print(f'Переменная ключ словаря {key=}\t {type(key)=}\t {getsizeof(key)=}\n')
                    print(f'Переменная значение словаря {value=}\t {type(value)=}\t {getsizeof(value)=}\n')
                    memory += getsizeof(key)
                    memory += getsizeof(value)
            elif not isinstance(i, str):
                print(f'Коллекция {i=}\t {type(i)=}\t {getsizeof(i)=}\n')
                memory += getsizeof(i)
                for j in i:
                    print(f'Переменная коллекции {j=}\t {type(j)=}\t {getsizeof(j)=}\n')
                    memory += getsizeof(j)
            else:
                print(f'Переменная {i=}\t {type(i)=}\t {getsizeof(i)=}\n')
                memory += getsizeof(i)
        else:
            # для строк
            print(f'Переменная {i=}\t {type(i)=}\t {getsizeof(i)=}\n')
            memory += getsizeof(i)

    return f'Память программы {memory=}'


print(memory_size(first_test))
print(memory_size(second_test))
print(memory_size(third_test))



"""
Windows 10 64 bit
Python 3.8.5 32 bit

Первый вариант:
Память программы memory=302
Второй вариант:
Память программы memory=974
Третий вариант:
Память программы memory=302

Исходя из результатов, в плане использования памяти первый вариант не отличается от третьего.
Второй же вариант из-за использование очереди тратит памяти в несколько раз больше.
Список из 10 элементов тратит 92, а очередь с таким же количеством элементов - 312.
Вывод: для список экономнее очереди.
"""
