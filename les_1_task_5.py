"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят,
и сколько между ними находится букв.
"""

first_latter = input('Введите первый символ')
second_latter = input('Введите второй символ')
first = ord(first_latter) - 96
second = ord(second_latter) - 96
if first > second:
    print("Попытка провалена((")
else:
    between = second - first
    print(f'{first_latter} = {first}'
          f'\n{second_latter} = {second}'
          f'\nразница = {between}')
