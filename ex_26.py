'''Задача 32:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''


def deg(n, d):
    if (d == 1):
        return (n)
    if (d != 1):
        return (n * deg(n, d - 1))


num = int(input("Введите число: "))
degree = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", deg(num, degree))
