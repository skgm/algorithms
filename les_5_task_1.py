"""
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict, deque

n = int(input('Введите количество компаний: '))
d = defaultdict(list)
sum_ = 0

for i in range(n):
    name = input(f'\nВведите название {i + 1}-ой компании: ')
    for j in range(4):
        m = int(input(f'Введите прибыль {j + 1}-го квартала: '))
        d[name].append(m)
        sum_ += m

avr = sum_ // 2
print(f'\nОбщая прибыль: {sum_}')
print(f'Средния прибыль: {avr}\n')

# вариант с очередью
# my_list = deque()
#
# for key, value in d.items():
#     if sum(value) < avr:
#         my_list.append(f'У компании {key} прибыль ниже среднего')
#     else:
#         # Впервую очередь принтятся прибыльные компании
#         my_list.appendleft(f'У компании {key} прибыль выше среднего')
# print(my_list)
# for i in my_list:
#     print(i, '\n')

good = 'Прибыль выше среднего'
bad = 'Прибыль ниже среднего'
my_dict = defaultdict(list)
for key, value in d.items():
    if sum(value) < avr:
        my_dict[bad].append(key)

    else:
        my_dict[good].append(key)


for key, value in my_dict.items():
    if key == good:
        print(f'Прибыль выше среднего у компаний:\n')
        print(*value)

print('-' * 100)

for key, value in my_dict.items():
    if key == bad:
        print(f'Прибыль ниже среднего у компаний:\n')
        print(*value)




