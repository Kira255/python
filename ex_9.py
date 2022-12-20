'''Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.'''
N = int(input('Введтие число N: '))
f = open('file.txt')
arr = []
mul = 1
for i in range(-N, N + 1):
    arr.append(i)
print(arr)
for line in f:
    mul = mul * arr[int(line)]
print(mul)
