"""
задание 2
https://drive.google.com/file/d/1B9FDnoQ4aIkXoWxigYlyjJfASKGzcrGb/view?usp=sharing

Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""

first = 5
second = 6
print(f'{first=}\nfirst_bin = {bin(5)}'
      f'\n{second=}\nsecond_bin = {bin(6)}')
a = first & second
b = first | second
c = first ^ second
print(f'{a = } \na_bin = {bin(a)}'
      f'\n{b = } \nb_bin = {bin(b)}'
      f'\n{c = } \nc_bin = {bin(c)}')
