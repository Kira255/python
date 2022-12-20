'''Реализуйте алгоритм перемешивания списка.'''
import random
list_original = [1, 2, 3]
list = list_original[:]
list_length = len(list)
for i in range(list_length):
    index = random.randint(0, list_length - 1)
    temp = list[i]
    list[i] = list[index]
    list[index] = temp
print(list)
