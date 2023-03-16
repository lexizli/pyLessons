# Программа по управлению телефонным справочником.
#
# Формат файла, в котором хранится справочник — csv (текстовый файл с разделителями). Разделитель — запятая Кодировка — utf-8
#
# Поля справочника:
#
# id — уникальный идентификатор (вопрос — что делать с ним при удалении данных)
# firstname — имя, кириллица, как минимум первая буква прописная
# patronymic — отчество, кириллица, как минимум первая буква прописная
# lastname — фамилия, кириллица, как минимум первая буква прописная
# phone — телефонный номер, формат вывода +7(ddd)ddd-dd-dd, хранения +7dddddddddd
# Функции программы:
#
# Вывод всех записей (предлагаю сортировать по фамилии и выводить по n строк)
# Поиск записи (по любой части)
# Добавление записи
# Редактирование записи (что можем менять?)
# Удаление записи
# Экспорт в текстовый файл
# Импорт из текстового файла (с парсингом?)
# Конец работы
#
# id;firstname;patrinymic;lastname;phone
#



from os import path
import csv

filename = "phones.csv"
last_id = 0
all_data = []


def show_all():
    if all_data:
        # print(*all_data, sep="\n")
        records = len(all_data)
        i = 0
        while i <= records:
            j = 0
            while j < 10:
                print(all_data[i])
                i += 1
                j += 1
            if input('More? 1 — Yes > ') != '1':
                break

        print(records)
    else:
        print("No records yet")

def search():
    pass

def add_new_contact():
    pass

def edit():
    pass

def delete():
    pass

def imp():
    pass

def read_csv_to_list(listname, filename, last_id):
    r_file = open(filename, encoding='utf-8')
    file_reader = csv.DictReader(r_file, delimiter=";")

    for row in file_reader:
        listname.append(row['userid'] + ' ' + row['firstname'] + ' '
                        + row['patrinymic'] + ' ' + row['lastname'] + ' ' + row['phone'])
    last_id = int(row['userid'])
    r_file.close()


def main_menu():
    play = True

    while play:
        read_csv_to_list(all_data, filename, last_id)
        answer = input("\nPhone book. Select operation:\n\n"
                       "1. Show all\n"
                       "2. Search\n"
                       "3. Add a record\n"
                       "4. Edit\n"
                       "5. Delete\n"
                       "6. Export\n"
                       "7. Import\n"
                       "8. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                search()
            case "3":
                add_new_contact()
            case "4":
                edit()
            case "5":
                delete()
            case "6":
                export()
            case "7":
                imp()
            case "8":
                play = False
            case _:
                print("Try again!\n")


main_menu()