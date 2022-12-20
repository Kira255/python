'''Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.'''
f = open('file.txt')
arr = []
mul = 1
for i in range(-5, 6):
    arr.append(i)
print(arr)
for line in f:
    mul = mul * arr[int(line)]
print(mul)
