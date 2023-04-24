from model import NotesDatabase
import datetime

now = datetime.datetime.now()

methods = NotesDatabase()

while True:
    print("Чтобы создать заметку, введите: 1.\nЧтобы обновить заметку, введите: 2.\nЧтобы удалить заметку, введите: 3.\nЧтобы прочитать заметки, введите: 4.\nЧтобы выйти, введите: 5.")
    try:
        number = int(input('Введите номер: '))
        if number == 1:
            id = int(input('Введите номер заметки: '))

            notes_name = input('Введите название: ')
            notes_subject = input('Введите тему: ')
            notes_content = input('Введите содержание: ')
            time = now.strftime("%d-%m-%Y %H:%M")
            methods.createNote(id, notes_name, notes_subject,
                               notes_content, time)
        elif number == 2:
            id = int(input('Введите номер заметки для редактирования: '))

            methods.updateNote(id)
        elif number == 3:
            id = int(input('Введите номер заметки: '))
            methods.deleteNote(id)
        elif number == 4:
            methods.showAll()
        elif number == 5:
            break
    except Exception as e:
        print(e)
