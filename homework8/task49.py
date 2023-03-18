# Программа по управлению телефонным справочником.
#
# Формат файла, в котором хранится справочник — csv (текстовый файл с разделителями).
# Разделитель — запятая Кодировка — utf-8
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
# userid;firstname;patrinymic;lastname;phone
#

from os import path, stat
import csv
import re

filename = "phones.csv"
last_id = 0
all_data = []


# Show records by row_counter if number of records more row_counter
def show_all(row_counter=10):
    if all_data:
        # print(*all_data, sep="\n")
        records = len(all_data)
        i = 0
        while i < records:
            j = 0
            while j < row_counter and i < records:
                print(all_data[i])
                i += 1
                j += 1
            ans = input('More? Y — Yes > ').lower()
            if ans != 'y' and ans != 'н':
                break
    else:
        print("No records yet")


# Search records by any part
def search(lissy, instr):   # find number
    founded = len([x for x in lissy if instr in x])
    if founded > 0:
        print(f'Founded {founded}', end="\n\t")
        print(*[x for x in lissy if instr in x], sep="\n\t")
    else:
        print('No records founded')


def add_new_contact():
    global last_id
    array = ["firstname", "patrinymic", "lastname", "phone"]
    string = ""
    for i in array:
        string += input(f"Enter {i} > ") + " "

    all_data.append(f"{last_id} {string}\n")

    last_id += 1


def edit():
    pass


# delete data not userid
def delete():
    id_for_clear = int(input('What record to delete? Input ID, please >'))-1
    print(all_data[id_for_clear])
    really = input('Delete this record? Press Y for yes > ').lower()
    if really == 'y' or really == 'н':
        all_data[id_for_clear] = str(id_for_clear+1) + ' [deleted] [deleted] [deleted] [deleted]'


def imp():
    pass


# export all_data to text file
def export():
    global all_data
    file_for_export = input('File name for export >')
    only_name = re.match('^[a-zA-Z0-9_-]*', file_for_export).group()
    if len(only_name) == 0:
        print("Sorry, I can't use this file name")
    filename_to_export = only_name + '.txt'
    if len(all_data) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('userid firstname patrinymic lastname phone\n')
            for i in all_data:
                fe.write(i+'\n')


# def to_phone_number(stri):
#     return (f'{stri[:2]}({stri[2:5]}){stri[5:8]}-{stri[8:10]}-{stri[10:12]}')


def read_csv_to_list(filename):
    global all_data, last_id
    all_data = []
    if not path.exists(filename):
        # print("No file exists")
        # return -1
        with open(filename, "w", encoding="utf-8") as _:
            pass
    else:
        r_file = open(filename, encoding='utf-8')
        file_reader = csv.DictReader(r_file, delimiter=",")
        if stat(filename).st_size != 0:
            for row in file_reader:
                all_data.append(row['userid'] + ' ' + row['firstname'] + ' '
                                + row['patrinymic'] + ' ' + row['lastname'] + ' ' + row['phone'])
            last_id = int(row['userid'])+1
        r_file.close()


def wr_csv(filename):  # write file
    global all_data
    csvfile = open(filename, 'w', newline='')
    fieldnames = ['userid', 'firstname', 'patrinymic', 'lastname', 'phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in all_data:
        nline = x.split()
        if ' [deleted] [deleted] [deleted] [deleted]' in x or len(x.split()) == 1:
            # nline = x.split()
            writer.writerow(
                {'userid': nline[0],
                 'firstname': '',
                 'patrinymic': '',
                 'lastname': '',
                 'phone': ''})
        else:
            # nline = x.split()
            writer.writerow(
                {'userid': nline[0],
                 'firstname': nline[1],
                 'patrinymic': nline[2],
                 'lastname': nline[3],
                 'phone': nline[4]})
    csvfile.close()


def main_menu():
    play = True

    while play:
        if read_csv_to_list(filename):
            break
        answer = input("\nPhone book. Select operation:\n\n"
                       "1. Show all\n"
                       "2. Search\n"
                       "3. Add a record\n"
                       "4. Edit\n"
                       "5. Delete\n"
                       "6. Export\n"
                       "7. Import\n\n"
                       "0. Exit\n")
        match answer:
            case "1":
                show_all()
                # print(last_id)
            case "2":
                to_find = input('What do you search ? > ')
                search(all_data, to_find)

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
            case "0":
                play = False
            case _:
                print("Try again!")
        wr_csv(filename)

main_menu()

