'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
from random import randint
import itertools

k = int(input('Введите степень: '))


def coeff(k):
    coeff = [randint(0, 100) for i in range(k + 1)]
    while coeff[0] == 0:
        coeff[0] = randint(1, 100)
    return coeff


def polynomial(k, coeff):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        coeff, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = coeff(k)
p = polynomial(k, ratios)
print(p)

with open('ex_19.txt', 'w') as data:
    data.write(p)
