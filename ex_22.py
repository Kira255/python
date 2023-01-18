'''Создайте программу для игры с конфетами человек против человека. 
Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. 
Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил'''

from random import randint


def dat(name):
    x = int(
        input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def pr(name, k, counter, value):
    print(
        f"{name} взял {k} конфет, теперь у него {counter}. Осталось {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if flag:
        k = dat(player1)
        counter1 += k
        value -= k
        flag = False
        pr(player1, k, counter1, value)
    else:
        k = dat(player2)
        counter2 += k
        value -= k
        flag = True
        pr(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
