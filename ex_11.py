'''Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
a = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(a), 2):
    sum = sum + a[i]
print(sum)
