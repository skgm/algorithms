"""
Матрица 5x4 заполняется вводом с клавиатуры,
кроме последних элементов строк.
Программа должна вычислять сумму введенных
элементов каждой строки и записывать ее
в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

N = 4
M = 5

array = [[' - ' for _ in range(N)] for _ in range(M)]

for i in range(len(array)):
    summ = 0
    for j in range(len(array[i])):
        if j != N - 1:
            num = int(input(f'Введите число под {j}-м индексом в строке'))
            array[i][j] = num
            print(array, '\n')
            summ += num
        else:
            array[i][j] = summ
            print(f'Сумма чисел в {i + 1}-ой строке = {summ}')
            print(array)

print('\n'.join([''.join(['%s\t' % i for i in row]) for row in array]))
