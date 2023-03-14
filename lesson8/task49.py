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
#     удалить телефонный номер
#     найти телефонный номер по фамилии (имени?)
#     выйти



# file_codes = open('kodes_till_03_07_2023.csv')
# new_list = open('new_list.csv', 'w')
# delimiter1 = '; "'
# delimiter2 = '"; "'
# delimiter3 = '"\n'
#
import csv

def find_tel(lissy, instr):
    print([x for x in lissy if instr in x])

def wr_csv(lissy, filename):
    csvfile = open(filename, 'w', newline='')
    fieldnames = ['Name', 'Secname', 'Lastname', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in lissy:
        nline = x.split()
        writer.writerow(
            {'Name': nline[0], 'Secname': nline[1], 'Lastname': nline[2], 'Phone': nline[3]})
    csvfile.close()


r_file = open("phones.csv", encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=",")

tels = []

for row in file_reader:
    tels.append(row['Name'] + ' ' + row['Secname'] + ' ' + row['Lastname'] + ' ' + row['Phone'])




# r_file.close()

# csvfile = open('phones1.csv', 'w', newline='')
# fieldnames = ['Name', 'Secname', 'Lastname', 'Phone']
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
# writer.writeheader()
# for row in file_reader:
#     print(row)
#     print(f'{row["Phone"]} — {row["Lastname"]}')
#     writer.writerow(row)
#
# writer.writerow({'Name': 'Антуанетта', 'Secname': 'Ипполитовна', 'Lastname': 'Запорова', 'Phone': '+70019991122'})
#
# csvfile.close()


print(sorted(tels))

wr_csv(sorted(tels), "newfile.csv")

find_tel(tels, "Анип")


