# with open('kodes_till_28_02_2023.csv') as file_kodes:
#     for line in file_kodes:
#         print(line.replace('"','').split(";")[1])  # end='' опускает лишний символ новой строки
#         print(line)

import csv
from datetime import datetime
import time

start_time = datetime.now()

with open("kodes_till_28_02_2023.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ";")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0

#    Считывание данных из CSV файла

    # for row in file_reader:
    #     if count == 0:
    #         # Вывод строки, содержащей заголовки для столбцов
    #         print(f'Файл содержит столбцы: {", ".join(row)}')
    #     # Вывод строк
    #     if row["Product code"] == "475T-FAS-90|52-54_182-188":
    #         print(f' {row["Product code"]} - {row["Product name"]}')
    #     count += 1
    #     # if count == 10:
    #     #     break
    # print(f'Всего в файле {count + 1} строк.')

    bumba = list(file_reader)

#for item in bumba:
    print([bumba_val for bumba_val in bumba if bumba_val["Product code"] == "475T-FAS-90|52-54_182-188"])

# time.sleep(5)
print(datetime.now() - start_time)

# file_kod = open('kodes_till_28_02_2023.csv')
# print(type(file_kod))
#
# print([bumba_val for bumba_val in file_kod if file_kod["Product code"] == "475T-FAS-90|52-54_182-188"])




