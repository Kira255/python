def get_str():
    st = int(input('Это информационная система позволяющая работать с учениками школы: чтобы ввести фамилию и имя (1), чтобы добавить предмет (2), чтобы добавить оценку (3), чтобы вывести список учеников (4), чтобы вывести оценки ученика (5), чтобы выйти (6): '))
    return st


def input_st():
    name = input('Введите имя и фамилю: ')
    return name


def input_pr():
    pr = input('Введите предмет: ')
    return pr


def input_mark():
    name = input('Введите имя и фамилю: ')
    pr = input('Введите предмет: ')
    mark = input('Введите оценку: ')
    return name, pr, mark


def get_name():
    name = input('Введите имя и фамилю: ')
    return name
