"""
По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков.
Если такой треугольник существует, то определить,
является ли он разносторонним,
равнобедренным или равносторонним.
"""

first = int(input('Введите длину первой стороны'))
second = int(input('Введите длину второй стороны'))
third = int(input('Введите длину третьей стороны'))

if first + second > third and first + third > second and second + third > first:
    if first == second and second == third:
        print(f'Треугольник со сторонами {first, second, third} существует, он равносторонний')
    elif first == second or second == third or first == third:
        print(f'Треугольник со сторонами {first, second, third} существует, он равнобедренный')
    else:
        print(f'Треугольник со сторонами {first, second, third} существует, он разносторонний')
else:
    print(f'Треугольник со сторонами {first, second, third} не существует')