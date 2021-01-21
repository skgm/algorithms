"""
задание 1
https://drive.google.com/file/d/1CzrRsFRQF44DGfoJ3vSTcVAjbeYRHSdT/view?usp=sharing
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
"""

num = int(input('Введите трехзначное число'))
first = num // 100
second = num // 10 % 10
third = num % 10
summary = first + second + third
product = first * second * third
print(f'{first = }, {second = }, {third = }')
print(f'{summary = }, {product = }')


