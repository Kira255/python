'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''
number = int(input("Введите натуральное число: "))
for i in range(1, number+1):
    if (number % i == 0):
        print(i)
