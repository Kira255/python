'''Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15'''
n = int(input('Введите число элементов: '))
x = int(input('Введите первый элемент: '))
d = int(input('Введите шаг: '))
print(*range(x, x + d * n, d))