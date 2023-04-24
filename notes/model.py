import json


class NotesDatabase:

    def createNote(self, serial_no, name, subject, content, time):
        note = {
            'count': serial_no,
            'page': [{
                'name': name,
                'subject': subject,
                'content': content,
                'time': time
            }
            ]
        }

        try:
            data = json.load(open('notes.json'))
        except:
            data = []

        data.append(note)

        with open('notes.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def showAll(self):
        data = json.load(open('notes.json'))
        for i in range(len(data)):
            c = data[i]['count']
            print(f'Номер заметки {c}')
            for j in data[i]['page']:
                print('Название')
                print(j['name'])
                print('Тема')
                print(j['subject'])
                print('Содержание')
                print(j['content'])
                print('Дата и время создания')
                print(j['time'])
                print('---------------------------------------------------')

    def updateNote(self, s_no):
        upChoice = int(input(
            "Чтобы изменить название, введите: 1.\nЧтобы изменить тему, введите: 2.\nЧтобы изменить содержание, введите: 3.\nВведите номер: "))
        data = json.load(open('notes.json'))
        note = data[s_no - 1]

        if upChoice == 1:
            notes_name = input('Введите новое название: ')
            d = note['page']
            d[0]['name'] = notes_name

            with open('notes.json', 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

        elif upChoice == 2:
            notes_subject = input('Введите новую тему: ')
            d = note['page']
            d[0]['subject'] = notes_subject

            with open('notes.json', 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

        elif upChoice == 3:
            notes_content = input('Введите новое содержание: ')
            d = note['page']
            d[0]['content'] = notes_content

            with open('notes.json', 'w') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

        else:
            print('Введите корректный номер: ')

    def deleteNote(self, s_no):
        data = json.load(open('notes.json'))
        data.pop(s_no - 1)
        with open('notes.json', 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
