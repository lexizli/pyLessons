'''
Формирование запроса через API Озона

На входе файл с FBS OZON SKU ID (код товара)

1. Нужно сформировать массив кодов товара по 500 штук
'''
import csv

ozon = 'sku.csv'
r_file = open(ozon, encoding='utf-8')
ozon_current = csv.DictReader(r_file, delimiter=";", quotechar='"')

# Создаем список подмассивов
sub_arrays = []


# Разбиваем исходный массив на подмассивы по 500 элементов
counter = 0
query_string = ""

for row in ozon_current:

    if counter < 500:
        query_string = query_string + '"' + str(row['FBS OZON SKU ID']) + '", '
        counter += 1
    else:
        sub_arrays.append(query_string)
        counter = 0
        print(query_string + "\n")
        query_string = ""

sub_arrays.append(query_string)
print(query_string + "\n")