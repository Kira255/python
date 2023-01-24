import iport
import xport


def v():
    c = iport.inter()
    if c == 1:
        iport.in_put()
    elif c == 2:
        xport.out_put()
    else:
        input('Некорректный ввод данных.')
