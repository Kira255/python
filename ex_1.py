'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
и проверяет, является ли этот день выходным.
- 6 -> да
- 7 -> да
- 1 -> нет'''
day = int(input('Введите номер дня недели: '))
if day == 6 or day == 7:
    print('да')
elif 1 <= day <= 5:
    print('нет')
else:
    print('Нужно ввести число в диапазоне от 1 до 7 включительно.')
