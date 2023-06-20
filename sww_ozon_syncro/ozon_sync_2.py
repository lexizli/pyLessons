#
#   Проверяет файл остатков, выгруженный из 1с stock_out.csv
#
#   файл должен лежать в рабочем каталоге, так как доступ по https не работает из-за кривого SSL-сертификата
#
#   Формат: csv с разделителем, разделитель — ;
#   Есть бесполезные строки, названия складов, их нужно удалить.
#   Могут быть товары без штрихкодов, их нужно вывести в отдельный файл ошибок
#   Дубли штрихкодов вывести в файл ошибок-дублей
#   В выходном файле следует поменять столбцы местами > штрихкод, количество, наименование
#   и отсортировать его по штрихкоду
#
# Именование входных
# входные файлы должны находится в каталоге input
#  всего 4 файла:
#
# stock_out.csv — остатки склада SWW, выгруженные из 1С, только положительные остатки
# ozon_current.csv — остатки и заказанные товары из Озона
# order_items_for_syncro.csv — выгруженные из sww.com.ru зарезервированные товары (их нельзя показывать покупателям)
# products_stock_tikhvin.csv — текущие остатки товаров со статусом «вкл» из ИМ sww.com.ru
#
# рабочих:
# рабочие файлы должны находится в каталоге wrk, который каждый раз перед запуском процедуры следует очищать
#
# s_o_clear.csv — отсортированные остатки склада SWW без дублей (двойных кодов),
#                      добавлена строка заголовков полей, чтоб работать с форматом CSV
# alert_s_o_doubles.csv — дублированные штрихкоды (это ошибки, в норме этого файла не должно быть)

import csv
from os import path, stat
import ti_stock_prep
import clear

clear.clear()   # remove all files from work and output directories

# save array list_to_write to file filename_to_export with first string column_names
# save ordered from sww.com.ru goods to temporary file


def write_to_csv(list_to_write, filename_to_export, column_names):
    if len(list_to_write) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write(column_names)
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()


filename = 'input/stock_out.csv'

if not path.exists(filename):
    exit('File stock_out.csv not exists')
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.readlines()
    r_file.close()

s_o_head_and_sorted = []

for line in file_temp:
    kwo = line.split(';')
    if len(kwo) == 3:
        s_o_head_and_sorted.append(str(kwo[2].strip()) + ';' + str(kwo[1]) + ';' + str(kwo[0]))

s_o_head_and_sorted.sort()

# Let's find double product codes, if exists (normally no)

s_o_clear = []      # data with single codes
alert_s_o_doubles = []    # double codes for alert
prev_line = prev_product_code = ""
for line in s_o_head_and_sorted:
    splitted_line = line.split(";")
    current_product_code = str(splitted_line[0])
    if current_product_code == prev_product_code:
        alert_s_o_doubles.append(prev_line)
        alert_s_o_doubles.append(line)
    else:
        s_o_clear.append(line)
        prev_product_code = current_product_code
        prev_line = line

if len(s_o_clear) > 0:
    with open('wrk/s_o_clear.csv', 'w', encoding='utf-8') as fe:
        fe.write('product_code;stock;product_name\n')
        for i in range(len(s_o_clear)): fe.write(s_o_clear[i] + '\n')
    fe.close()

if len(alert_s_o_doubles) > 0:
    with open('out/alert_stock_out_doubles.csv', 'w', encoding='utf-8') as fe:
        fe.write('Внимание! В остатках склада есть двойные коды!\n')
        fe.write('product_code;stock;product_name\n')
        for i in range(len(alert_s_o_doubles)): fe.write(alert_s_o_doubles[i] + '\n')
    fe.close()

# now we can decrease stock for reserved on sww.com.ru goods  — order_items_for_syncro.csv
# data format in file:
# Order ID;Item ID;Product code;Quantity
# "42363";"2816000254";"2001459883358";"3"
# we need two last columns Product code and Quantity
# if there is the same Product code, we have to sum Quantity and output only one string for every Product code

filename = 'input/order_items_for_syncro.csv'

if not path.exists(filename):
    exit('File order_items_for_syncro.csv not exists')
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.readlines()
    r_file.close()

# step 1 — selecting product code and quantity
order_items_for_syncro = []
for line in file_temp:
    kwo = line.split(';')
    if kwo[0] == 'Order ID':
        # print('Skip header')
        pass
    else:
        order_items_for_syncro.append(str(kwo[2]) + ';' + str(kwo[3].strip()))

order_items_for_syncro.sort()

# step 2 — summ quantities for same product code
sww_ordered_sum = []
prev_ordered_row = prev_ordered_code = ""

cleared = []

for line in order_items_for_syncro:     # we have to delete double quotes, them interfere
    line_cleared = line.replace('"', '')
    cleared.append(line_cleared)

order_items_for_syncro = cleared

sww_no_orders = len(order_items_for_syncro) < 1  # if no orders from SWW — Important! --------------------------

if not sww_no_orders:
    for line in order_items_for_syncro:
        kwo = line.split(';')

        if len(prev_ordered_row) == 0:  # if first dataset, put it in buffer
            prev_ordered_row = line
            prev_ordered_code = str(kwo[0])
            quan = int(kwo[1])
        else:
            current_ordered_code = str(kwo[0])
            if current_ordered_code == prev_ordered_code:  # if product code the same as previous
                quan += int(kwo[1])  # sum ordered quantity
            else:
                # current buffer to dataset
                sww_ordered_sum.append(prev_ordered_code + ';' + str(quan))
                # put next dataset in buffer
                prev_ordered_row = line
                prev_ordered_code = str(kwo[0])
                quan = int(kwo[1])
    sww_ordered_sum.append(prev_ordered_code + ';' + str(quan))    # the last buffer to dataset
else:
    sww_ordered_sum.append("" + ';' + "0")

write_to_csv(sww_ordered_sum, 'wrk/sww_ordered_sum.csv', 'product_code;ordered\n')

# now time to work with file from Ozon

ozon = 'input/ozon_current.csv'
r_file = open(ozon, encoding='utf-8')
ozon_current = csv.DictReader(r_file, delimiter=";", quotechar='"')

# select columns, sort, write to temp files
ozon_ordered = []
ozon_stock = []
if stat(ozon).st_size != 0:
    for row in ozon_current:
        ozon_stock.append(str(row['\ufeff"Артикул"']) + ';'
                          + str(row['Доступно на "Тихвин, Мебельная 1", шт']))
        if int(row['Зарезервировано на "Тихвин, Мебельная 1", шт']) > 0:
            ozon_ordered.append(str(row['\ufeff"Артикул"'])
                         + ';' + str(row['Зарезервировано на "Тихвин, Мебельная 1", шт']))

r_file.close()
ozon_stock.sort()
write_to_csv(ozon_stock, 'wrk/ozon_stock.csv', 'product_code;stock\n')
ozon_ordered.sort()

ozon_no_orders = len(ozon_ordered) < 1  # if no orders from Ozon — Important! --------------------------

if ozon_no_orders:
    ozon_ordered.append("" + ';' + "")
write_to_csv(ozon_ordered, 'wrk/ozon_ordered.csv', 'product_code;ordered\n')

# now we can determine the goods available for ordering in the warehouse sww
# get data from stock_out_clear, ordered_sww_sum.csv and ozon_ordered.csv
# decrease stock value on ordered and ozon_ordered
#
# Important! ---------------------------------------------------------------
# sww_no_orders = True if no orders from SWW
# ozon_no_orders = True if no orders from Ozon

fname = 'wrk/s_o_clear.csv'
r_file = open(fname, encoding='utf-8')
s_o_clear = csv.DictReader(r_file, delimiter=";", quotechar='"')

fname = 'wrk/ozon_stock.csv'
r_file_s_ozon = open(fname, encoding='utf-8')
ozon_stock = csv.DictReader(r_file_s_ozon, delimiter=";", quotechar='"')
ozon_stock_row = ozon_stock.__next__()
current_ozon_stock_product_code = ozon_stock_row['product_code']
current_ozon_stock = ozon_stock_row['stock']

if not sww_no_orders:
    fname = 'wrk/sww_ordered_sum.csv'
    r_file_o_sww = open(fname, encoding='utf-8')
    sww_ordered_sum = csv.DictReader(r_file_o_sww, delimiter=";", quotechar='"')

    ordered_current_sww = sww_ordered_sum.__next__()
    current_sww_product_code = ordered_current_sww['product_code']    # product code from first string
else:
    print("В магазине SWW нет заказов в статусах «открыт» или «обработан»")

if not ozon_no_orders:
    fname = 'wrk/ozon_ordered.csv'
    r_file_o_ozon = open(fname, encoding='utf-8')
    ozon_ordered = csv.DictReader(r_file_o_ozon, delimiter=";", quotechar='"')

    ordered_current_ozon = ozon_ordered.__next__()
    current_ozon_product_code = ordered_current_ozon['product_code']  # product code from first string
else:
    print("В Озоне нет заказов")

sww_available = []
ozon_alert = []     # for product codes in ozon if ozon_stock > 0
ordered_sww_toomuch = []    # for ordered from sww if it absent in sww stock
ordered_ozon_toomuch = []   # for ordered from ozon if it absent in sww stock
sww_minused = []        # full sww stock data with decreasing goods quantity
sww_for_compare = []    # sww stock data which consistent with ozon stock
sww_to_ozon_syncro = []     # data for synchronisation
sww_position = 0

more_iteration_ordered_sww = True
more_iteration_ordered_ozon = True
more_iteration_ozon = True


for sww_row in s_o_clear:
    # сохраняем остаток склада в буфер

    temp_sww_row_stock = int(sww_row['stock'])

    # минусуем из доступных остатков склада SWW товары, заказанные на sww.com.ru
    if not sww_no_orders:
        if more_iteration_ordered_sww:
            if sww_row['product_code'] > current_sww_product_code:
                if int(ordered_current_sww['ordered']) != 0:  # if present order in sww, but it absent in sww stock
                    ordered_sww_toomuch.append(str(current_sww_product_code) + ';' + str(ordered_current_sww['ordered']))
                try:
                    ordered_current_sww = sww_ordered_sum.__next__()
                    current_sww_product_code = ordered_current_sww['product_code']  # product code from next string
                except StopIteration:
                    more_iteration_ordered_sww = False

            if sww_row['product_code'] == current_sww_product_code:
                sww_row['stock'] = str(int(sww_row['stock']) - int(ordered_current_sww['ordered']))
                if int(sww_row['stock']) < 0:
                    ordered_sww_toomuch.append(str(current_sww_product_code) + ';' + str(ordered_current_sww['ordered']))
                try:
                    ordered_current_sww = sww_ordered_sum.__next__()
                    current_sww_product_code = ordered_current_sww['product_code']  # product code from next string
                except StopIteration:
                    more_iteration_ordered_sww = False

    # затем минусуем из доступных остатков склада SWW товары, заказанные на Озоне
    # ordered_current_ozon
    # current_ozon_product_code

    if not ozon_no_orders:
        if more_iteration_ordered_ozon:
            if sww_row['product_code'] > current_ozon_product_code:
                if int(ordered_current_ozon['ordered']) != 0:  # if present order in ozon, but it absent in sww stock
                    ordered_ozon_toomuch.append(str(current_ozon_product_code) + ';'
                                                + str(ordered_current_ozon['ordered']))
                try:
                    ordered_current_ozon = ozon_ordered.__next__()
                    current_ozon_product_code = ordered_current_ozon['product_code']  # product code from next string
                except StopIteration:
                    more_iteration_ordered_ozon = False

            if sww_row['product_code'] == current_ozon_product_code:
                sww_row['stock'] = str(int(sww_row['stock']) - int(ordered_current_ozon['ordered']))
                if int(sww_row['stock']) < 0:
                    ordered_ozon_toomuch.append(str(current_sww_product_code) + ';'
                                                + str(ordered_current_ozon['ordered']))
                try:
                    ordered_current_ozon = ozon_ordered.__next__()
                    current_ozon_product_code = ordered_current_ozon['product_code']  # product code from next string
                except StopIteration:
                    more_iteration_ordered_ozon = False

    # теперь сравниваем остатки на Озоне и текущие, и если они не равны, добавляем строку в массив для синхронизации
    # current_ozon_stock_product_code = ozon_stock_row['product_code']
    # current_ozon_stock = ozon_stock_row['stock']

    while sww_row['product_code'] > current_ozon_stock_product_code and more_iteration_ozon:
        if int(ozon_stock_row['stock']) != 0:  # if present stock in Ozon, but it absent in sww
            ozon_alert.append(str(current_ozon_stock_product_code) + ';' + str(ozon_stock_row['stock']))
        try:
            ozon_stock_row = ozon_stock.__next__()
            current_ozon_stock_product_code = ozon_stock_row['product_code']  # product code from next string
        except StopIteration:
            more_iteration_ozon = False
        # print("290 — current_ozon_stock_product_code", current_ozon_stock_product_code)
        if sww_row['product_code'] == current_ozon_stock_product_code:
            break

    if sww_row['product_code'] == current_ozon_stock_product_code:
        sww_for_compare.append((str(sww_row['product_code']) + ';' + str(sww_row['stock']) + ';' + sww_row['product_name']))
        if int(sww_row['stock']) != int(ozon_stock_row['stock']):
            sww_to_ozon_syncro.append((str(sww_row['product_code']) + ';' + str(sww_row['stock'])))
        if more_iteration_ozon:
            try:
                ozon_stock_row = ozon_stock.__next__()
                current_ozon_stock_product_code = ozon_stock_row['product_code']  # product code from next string
            except StopIteration:
                more_iteration_ozon = False

# # debug print changed stock availability for order
#     if int(sww_row['stock']) != temp_sww_row_stock:     # if changed
#         print(sww_row['stock'])

    # full sww stock data with decreasing goods quantity
    sww_minused.append(
        str(sww_row['product_code']) + ';' + str(sww_row['stock']) + ';' + sww_row['product_name'])

r_file.close()
r_file_s_ozon.close()
if not sww_no_orders:
    r_file_o_sww.close()
if not ozon_no_orders:
    r_file_o_ozon.close()

write_to_csv(sww_minused, 'wrk/sww_minused.csv', 'product_code;stock;product_name\n')
write_to_csv(sww_for_compare, 'wrk/sww_for_compare.csv', 'product_code;stock;product_name\n')
if len(sww_to_ozon_syncro) > 0:
    write_to_csv(sww_to_ozon_syncro, 'out/sww_to_ozon_syncro.csv', 'product_code;stock\n')

if len(ordered_sww_toomuch) > 0:
    write_to_csv(ordered_sww_toomuch, 'out/ordered_sww_toomuch.csv', 'product_code;reordered\n')
if len(ordered_ozon_toomuch) > 0:
    write_to_csv(ordered_ozon_toomuch, 'out/ordered_ozon_toomuch.csv', 'product_code;reordered\n')
if len(ozon_alert) > 0:
    write_to_csv(ozon_alert, 'out/ozon_alert.csv', 'product_code;more than in sww stock\n')

# OK, continue with Internet-shop stock
# input file — product_stock_tikhvin.csv

# first step — select useful data and sort by product_code

ti_stock_prep.tikhvin_stock_prepare()

fname = 'wrk/stock_tikhvin_prepared.csv'
prep_tikhvin = open(fname, encoding='utf-8')
stock_tikhvin_prepared = csv.DictReader(prep_tikhvin, delimiter=";", quotechar='"')

fname = 'wrk/sww_minused.csv'
sww = open(fname, encoding='utf-8')
sww_minused = csv.DictReader(sww, delimiter=";", quotechar='"')

sww_current = sww_minused.__next__()
sww_current_product_code = sww_current['product_code']  # product code from first string

more_iteration_minused = True

# Will synchronise only product's codes present in internet-shop

for_import = []     # array prepared for synchronisation

for product in stock_tikhvin_prepared:
    temp_tikhvin_stock = int(product['stock'])

    while product['product_code'] > sww_current_product_code and more_iteration_minused:
        try:
            sww_current = sww_minused.__next__()
            sww_current_product_code = sww_current['product_code']  # product code from next string
        except StopIteration:
            more_iteration_ozon = False
        # print("290 — current_ozon_stock_product_code", current_ozon_stock_product_code)
        if product['product_code'] == sww_current_product_code:
            break

    if product['product_code'] == sww_current_product_code:
        if product['stock'] != sww_current['stock']:
            for_import.append(str(sww_current['product_code']) + ';'
                              + str(sww_current['stock']) + ';' + product['product_name']
                              + ";ru;sww")
        try:
            sww_current = sww_minused.__next__()
            sww_current_product_code = sww_current['product_code']  # product code from next string
        except StopIteration:
            more_iteration_ozon = False
        # sww_current = sww_minused.__next__()
        # sww_current_product_code = sww_current['product_code']

write_to_csv(for_import, 'out/for_import_to_sww_com_ru.csv', 'Product code;Центральный склад (Warehouse);Product name;Language;Store\n')
