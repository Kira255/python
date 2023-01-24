def inter():
    cont = int(input(
        'Это телофонный справочник: чтобы ввести данные введите (1), чтобы вывести данные введите (2): '))
    return cont


def in_put():
    id = str(input('Введите id: '))
    name = str(input('Введите имя: '))
    sname = str(input('Введите фамилию: '))
    phone = str(input('Введите номер телефона: '))
    comment = str(input('Введите комментрий: '))
    res = id + ' ' + name + ' ' + sname + ' ' + phone + ' ' + comment
    f = open('Phonebook.txt', 'a')
    f.write(res + '\n')
    f.close
    return res
