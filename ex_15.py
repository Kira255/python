'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''
num = int(input('Введите число: '))


def get_fibonacci(n):
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    return fib


fibo_nums = get_fibonacci(num)
print(get_fibonacci(num))
