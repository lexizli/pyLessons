#
#   Проверяет файл остатков, выгруженный из 1с
#
#   файл должен лежать тут > https://sww.com.ru/stock/stock_out.csv
#
#   В начале проверить дату/время файла и вывести их в консоль — это что-то никак :-(
#
#   Формат: csv с разделителем, разделитель — ;
#   Есть бесполезные строки, названия складов, их нужно удалить
#   Могут быть товары без штрихкодов, их нужно вывести в отдельный файл ошибок
#   Дубли штрихкодов вывести в файл ошибок-дублей
#   В выходном файле следует столбцы местами > штрихкод, количество, наименование
#   и отсортировать его по штрихкоду
#


from os import path, stat
from os.path import getctime
import csv
import requests
from datetime import datetime

# today = datetime.today().strftime('%d-%m-%y-%H_%M_%S')
all_data = []


# добавляем наименования столбцов к выгрузке
def add_head(file_temp):
    filename_to_export = 'stock_out_head.csv'
    if len(file_temp) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_name;stock;product_code\n')
            fe.write(file_temp)
    fe.close()


def write_sorted(list_to_write):
    filename_to_export = 'stock_out_sorted.csv'
    if len(list_to_write) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_code;stock;product_name\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()


URL = 'https://sww.com.ru/stock/stock_out.csv'  # Тут каждый час обновляемые остатки склада из 1С
filename = 'stock_out.csv'                      # с таким именем сохраняем в рабочий каталог
response = requests.get(URL)

print(response)
print("Responce was printed \n\n\n")

# print(datetime.fromtimestamp(getctime('stock_out_sorted.csv')).strftime('%d-%m-%Y %H:%M:%S'))
# пытался получить метаданные файла,
# работает только с локальным файлом

if not path.exists(filename):
    print("No file exists")
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.read()
    file_temp = file_temp[1:]  # remove bom
    r_file.close()
    add_head(file_temp)

wrk_file = 'stock_out_head.csv'
r_file = open(wrk_file, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")
if stat(wrk_file).st_size != 0:
    for row in file_reader:
        if row['stock']:
            all_data.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
r_file.close()

all_data.sort()
write_sorted(all_data)

# will find same codes

all_clear = []
all_doubles = []
wrk_file = 'stock_out_sorted.csv'
r_file = open(wrk_file, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")
prev_code = ""
if stat(wrk_file).st_size != 0:
    for row in file_reader:
        current_code = str(row['product_code'])
        if current_code == prev_code:
            all_doubles.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
        else:
            all_clear.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
        prev_code = str(row['product_code'])
r_file.close()

print(all_doubles)
print(all_clear)


