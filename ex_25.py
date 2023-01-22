'''Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]'''
import random

mas = [random.randint(-50, 50) for i in range(random.randint(10, 20))]

print(*mas)

max = int(input("MAX = "))

min = int(input("MIN = "))

mas2 = []

if max >= min:

    for i in range(len(mas)):

        if max >= mas[i] and min <= mas[i]:

            mas2.append(i)

print("Кол-во:", len(mas2))

print("Индексы:", mas2)
