"""
https://patorjk.com/ - генератор АСИшных слов, картинок и чего угодно
Додаток буде сохранять заметки

This is my note, that I am takingon my laptop
- Created on 11.05.2026 17:06 * - типа выбранный (избранное)

1) Создать словарь и записать в него иформацию от пользователя
2) Написать йункцию которая будует выводит наше запись
3) Написать функцию которая будует выводить все добавленные записи
3) Написать цикл чтобы получать информацию от пользователя и реагировать на нее
4) Созранять все данные в файле - с изменением Жатой Временем
5) Формат будет список (list)
[("This is my note, that I am takingon my laptop", "11.05.2026 17:06")]
[("11.05.2026 17:06", ("This is my note, that I am takingon my laptop", "11.05.2026 17:06")]

{"text":"This is my note, that I am takingon my laptop", "creation_date": "11.05.2026 17:06"}

"""
from datetime import datetime

note_list = [] # {"text":"This is my note, that I am takingon my laptop", "creation_date": "11.05.2026 17:06"}
note_file = "notes.txt"

# Формат записи созданых НАТАЦИЙ в файл notes.txt - [Hello Note; 11.05.2026 17:06]

welcome_banner = '''
            _                     ___       _   
  /\  /\___| |_ __   ___ _ __    / __\ ___ | |_ 
 / /_/ / _ \ | '_ \ / _ \ '__|  /__\/// _ \| __|
/ __  /  __/ | |_) |  __/ |    / \/  \ (_) | |_ 
\/ /_/ \___|_| .__/ \___|_|    \_____/\___/ \__|
             |_|                                
'''
commands = """
1 -> exit - to exit the application
2 -> add_note - to add a new note
3 -> print_note [i] - to print note number i
4 -> print_all - to print all notes
5 -> help - to print this MENU
"""

def add_new_note(note_text)-> bool:
    note_creation_date = datetime.today()
    note_list.append({"text": note_text, "creation_date": note_creation_date})
    return True

def print_note(index: int):
    note = note_list [index]
    formatted_creation_date = note["creation_date"].strftime("%d.%m.%Y %H:%M")
    print(f"{note["text"]}\n- Created on {formatted_creation_date}\n")

def print_all_notes():
    for note_index in range(len(note_list)):
        print_note (note_index)

def save_notes():
    with open(note_file, "w") as file:
        for note in note_list:
            file.write(f"{note["text"]};{note["creation_date"]}\n")

def read_notes() -> list[dict]:
    note_list = []
    with open (note_file) as file:                                           # формат не указываем - так ка будет только чтение файла
        for line in file:                                                    # идем по записанным данным [Google NOW !!!;2026-05-13 10:54:15.635654]
            text, date = line.strip().split(";")                             # разбиваем полученные данные на ДВЕ части text и date, так же чистим формат строки      
            creation_date = datetime.strptime (date, "%Y-%m-%d %H:%M:%S.%f")
            note_list.append({"text": text, "creation_date":creation_date})
    return note_list

def init():
    global note_list                                    # определяем что будем работать с внешней ПЕРЕМЕННОЙ note_list
    note_list = read_notes()

    print(welcome_banner)
    print ("<<< hello and welcome to our app >>>")
    print (commands)

def main ():
    while True:
        command, *args = input ("Please ENTER your command (enter EXIT to stop): ").strip().split(" ")
        # .strip() - удаляет пробелы в начале и конце строки / .split(" ") - разбивает строку по пробелам и превращает её в список
        if command== "exit":
            print (">>> Goodbye! <<<")
            save_notes()
            break
        elif command == "add_note":
            text = input ("Please enter note text: ")
            if add_new_note (text):
                print("Note added successfully!\n")
            else:
                print ("\nError while ading a note!\n")
        elif command =="help":
            print(welcome_banner)
            print ("<<< hello and welcome to our app >>>")
            print (commands)
        elif command == "print_note":
            index = int (args[0]) - 1
            if index < 0 or index >= len(note_list):
                print ("Please enter a valid note number")
                continue
            print_note(index)

init()
main()

# print_all_notes()
# text = input ("Please enter note text: ")
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)
# add_new_note(text)

