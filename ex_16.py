'''Вычислить число c заданной точностью d
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''


def pi(d=0.001):
    s = 0
    c = 1
    sgn = 1
    while True:
        a = 4 / c
        s = s + sgn * a
        if a < d:
            return s
        sgn = -sgn
        c = c + 2


print(pi())
