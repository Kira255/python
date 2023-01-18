'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    k = 0
    l = 1
    for j in range(len(txt) // 2):
        for i in range(int(txt[k])):
            res = res + txt[l]
        l += 2
        k += 2
    return res


s = input("Введите текст для кодировки: ")
res = coding(s)
print(f"Текст после кодировки: {res}")
print(f"Текст после дешифровки: {decoding(res)}")
