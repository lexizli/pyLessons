# Задача №49.
# Создать телефонный справочник
# с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# общий цикл, внутри которого есть список команд:
#     прочитать справочник
#     сохранить справочник
#     добавить телефонный номер
#     найти телефонный номер по фамилии (имени?)
#     выйти

import csv


def find_tel(lissy, instr):   # find number
    print([x for x in lissy if instr in x])


def wr_csv(lissy, filename):  # write file
    csvfile = open(filename, 'w', newline='')
    fieldnames = ['Name', 'Secname', 'Lastname', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for x in lissy:
        nline = x.split()
        writer.writerow(
            {'Name': nline[0], 'Secname': nline[1], 'Lastname': nline[2], 'Phone': nline[3]})
    csvfile.close()

def read_csv_to_list(listname, filename):
    r_file = open(filename, encoding='utf-8')
    file_reader = csv.DictReader(r_file, delimiter=",")

    for row in file_reader:
        listname.append(row['Name'] + ' ' + row['Secname'] + ' ' + row['Lastname'] + ' ' + row['Phone'])

    r_file.close()

tels = []
read_csv_to_list(tels, 'phones.csv')

while True:
    comm = input('Input command (all, find, add, end) > ')
    if comm not in ('all', 'find', 'add', 'end'):
        print('Я не знаю такой команды ;-)')
    if comm == 'all':
        for row in tels:
            print(row)
    if comm == 'find':
        to_find = input('Кого ищешь? > ')
        find_tel(tels, to_find)
    if comm == 'add':
        tels.append(input('Введи через пробел фамилию, имя, отчество и номер телефона > '))
    if comm == 'end':
        break

wr_csv(sorted(tels), "phones.csv")



