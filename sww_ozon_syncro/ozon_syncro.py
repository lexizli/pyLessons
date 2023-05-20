#
#   Проверяет файл остатков, выгруженный из 1с stock_out.csv
#
#   файл должен лежать в рабочем каталоге, так как доступ по https не работает из-за кривого SSL-сертификата
#
#   Формат: csv с разделителем, разделитель — ;
#   Есть бесполезные строки, названия складов, их нужно удалить
#   Могут быть товары без штрихкодов, их нужно вывести в отдельный файл ошибок
#   Дубли штрихкодов вывести в файл ошибок-дублей
#   В выходном файле следует столбцы местами > штрихкод, количество, наименование
#   и отсортировать его по штрихкоду
#
import csv
from os import path, stat

# today = datetime.today().strftime('%d-%m-%y-%H_%M_%S')
all_data = []


# добавляем наименования столбцов к выгрузке и выводим данные во временный файл
def add_head(file_temp, filename_to_export):
    if len(file_temp) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_name;stock;product_code\n')
            fe.write(file_temp)
    fe.close()

# выводим отсортированные данные с измененным порядком столбцов во временный файл
def write_sorted(list_to_write, filename_to_export):
    if len(list_to_write) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_code;stock;product_name\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()

# выводим дубли если они есть во временный файл stock_out_doubles.csv
def write_doubles(list_to_write):
    filename_to_export = 'stock_out_doubles.csv'
    if len(list_to_write) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_code;stock;product_name\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()

# save ordered from sww.com.ru goods to temporary file
def write_ordered_sww(list_to_write, filename_to_export):
    if len(list_to_write) > 0:
        with open(filename_to_export, 'w', encoding='utf-8') as fe:
            fe.write('product_code;ordered\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()

# save ozon stock data from ozon to temporary file
def write_ozon_stock(list_to_write, filename_for_stock):
    if len(list_to_write) > 0:
        with open(filename_for_stock, 'w', encoding='utf-8') as fe:
            fe.write('product_code;ozon_stock\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
    fe.close()

# save ozon ordered data from ozon to temporary file
def write_ozon_ordered(list_to_write, filename_for_ordered):
    if len(list_to_write) > 0:
        with open(filename_for_ordered, 'w', encoding='utf-8') as fe:
            fe.write('product_code;ozon_ordered\n')
            for i in range(len(list_to_write)): fe.write(list_to_write[i] + '\n')
        fe.close()


filename = 'stock_out.csv'

if not path.exists(filename):
    print("No file exists")
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.read()
    file_temp = file_temp[1:]  # remove bom
    r_file.close()
    add_head(file_temp, 'stock_out_head.csv')

wrk_file = 'stock_out_head.csv'
r_file = open(wrk_file, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")
if stat(wrk_file).st_size != 0:
    for row in file_reader:
        if row['stock']:
            all_data.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
r_file.close()

all_data.sort()
write_sorted(all_data, 'stock_out_sorted.csv')

# will find same codes

all_clear = []
all_doubles = []
wrk_file = 'stock_out_sorted.csv'
r_file = open(wrk_file, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")
prev_row = prev_code = ""
if stat(wrk_file).st_size != 0:
    for row in file_reader:
        current_code = str(row['product_code'])
        if current_code == prev_code:
            all_doubles.append(str(prew_row['product_code']) + ';' + str(prew_row['stock']) + ';'
                               + prew_row['product_name'])
            all_doubles.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
        else:
            all_clear.append(str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])
        prev_code = str(row['product_code'])
        prew_row = row
r_file.close()

if len(all_doubles) == 0:
    print("OK, there are no doubles in stock file")
else:
    write_doubles(all_doubles)

# now we have sorted and clear from doubles array from stock — all_clear

write_sorted(all_clear, 'stock_out_clear.csv')

# now we can decrease stock for reserved on sww.com.ru goods  — order_items_for_syncro.csv
# data format in file:
# Order ID;Item ID;Product code;Quantity
# "42363";"2816000254";"2001459883358";"3"
# we need two last columns Product code and Quantity
# if there is the same Product code, we have to sum Quantity and output only one string for every Product code

ordered_sww = 'order_items_for_syncro.csv'
r_file = open(ordered_sww, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")

# step 1 — select columns and sort
ordered_sww_data = []
if stat(ordered_sww).st_size != 0:
    for row in file_reader:
        ordered_sww_data.append(str(row['Product code']) + ';' + str(row['Quantity']))
r_file.close()
ordered_sww_data.sort()
write_ordered_sww(ordered_sww_data, 'ordered_sww.csv')

# step 2 — summ quantities for same product code
ordered_sww_data_sum = []
prev_ordered_row = prev_ordered_code = ""
ordered_sww = 'ordered_sww.csv'
r_file = open(ordered_sww, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";")

if stat(ordered_sww).st_size != 0:
    for row in file_reader:
        if len(prev_ordered_row) == 0:  # if first dataset, put it in buffer
            prev_ordered_row = row
            prev_ordered_code = str(row['product_code'])
            quan = int(row['ordered'])
        else:
            current_ordered_code = str(row['product_code'])
            if current_ordered_code == prev_ordered_code:   # if product code the same as previous
                quan += int(row['ordered'])                 # sum ordered quantity
            else:
                # current buffer to dataset
                ordered_sww_data_sum.append(str(prev_ordered_row['product_code']) + ';' + str(quan))
                # put next dataset in buffer
                prev_ordered_row = row
                prev_ordered_code = str(row['product_code'])
                quan = int(row['ordered'])
    ordered_sww_data_sum.append(str(prev_ordered_row['product_code']) + ';' + str(quan))    # the last buffer to dataset
r_file.close()

write_ordered_sww(ordered_sww_data_sum, 'ordered_sww_sum.csv')

# now time to work with file from Ozon

ozon = 'ozon_current.csv'
r_file = open(ozon, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";", quotechar='"')

# step 1 — select columns and sort
ozon_ordered = []
ozon_stock = []
if stat(ozon).st_size != 0:
    for row in file_reader:
        ozon_stock.append(str(row['\ufeff"Артикул"']) + ';'
                          + str(row['Доступно на "Тихвин, Мебельная 1", шт']))
        if int(row['Зарезервировано на "Тихвин, Мебельная 1", шт']) > 0:
            ozon_ordered.append(str(row['\ufeff"Артикул"'])
                         + ';' + str(row['Зарезервировано на "Тихвин, Мебельная 1", шт']))

r_file.close()
ozon_stock.sort()
write_ozon_stock(ozon_stock, 'ozon_stock.csv')
ozon_ordered.sort()
write_ozon_ordered(ozon_ordered, 'ozon_ordered.csv')

# now we can determine the goods available for ordering in the warehouse sww
# get data from stock_out_clear, ordered_sww_sum.csv and ozon_ordered.csv
# decrease stock value on ordered and ozon_ordered

stock = 'stock_out_clear.csv'
r_file = open(stock, encoding='utf-8')
file_reader = csv.DictReader(r_file, delimiter=";", quotechar='"')

with open(stock, "r") as f: # count strings in stock_out_clear.csv
    reader = csv.reader(f)
    row_in_stock = sum(1 for row in reader)

ordered_sww = 'ordered_sww_sum.csv'
r_file_o_sww = open(ordered_sww, encoding='utf-8')
file_ordered_sww = csv.DictReader(r_file_o_sww, delimiter=";", quotechar='"')

with open(ordered_sww, "r") as f:   # count strings in ordered_sww_sum.csv
    reader = csv.reader(f)
    row_in_sww = sum(1 for row in reader)

ordered_ozon = 'ozon_ordered.csv'
r_file_o_ozon = open(ordered_ozon, encoding='utf-8')
file_ordered_ozon = csv.DictReader(r_file_o_ozon, delimiter=";", quotechar='"')

with open(ordered_ozon, "r") as f:  # count strings in ozon_ordered.csv
    reader = csv.reader(f)
    row_in_ozon = sum(1 for row in reader)

st_ozon = 'ozon_stock.csv'
r_file_s_ozon = open(st_ozon, encoding='utf-8')
file_st_ozon = csv.DictReader(r_file_s_ozon, delimiter=";", quotechar='"')

with open(st_ozon, "r") as f:   # count strings in ozon_stock.csv
    reader = csv.reader(f)
    row_in_ozon_st = sum(1 for row in reader)

# debug print
print("In sww stock — ", row_in_stock, " Ordered from sww — ", row_in_sww,
      " Ordered from Ozon — ", row_in_ozon, " Total in Ozon — ", row_in_ozon_st
      )

# step 1 — select columns and sort
sww_available = []
ordered_alert = []
ordered_alert_toomuch = []
current_sww = file_ordered_sww.__next__()
current_sww_pc  = current_sww['product_code']    # product code from first string
current_ozon = file_ordered_ozon.__next__()
current_ozon_pc = current_ozon['product_code']  # product code from first string
current_ozon_st = file_st_ozon.__next__()
current_ozon_st_pc = current_ozon_st['product_code']  # product code from first string
cur_sww_position = 7
cur_ozon_position = 3
cur_ozon_st_position = 4

sww_minused = []        # full sww stock data with decreasing goods quantity
sww_for_compare = []    # sww stock data which consistent with ozon stock
sww_to_ozon_syncro = []     # data for synchronisation
sww_position = 0

if stat(stock).st_size != 0:
    for row in file_reader:
        if row['product_code'] > current_sww_pc and cur_sww_position < row_in_sww:
            if int(current_sww['ordered']) != 0:     # if present order in sww, but it absent in sww stock
                ordered_alert_toomuch.append(str(current_sww_pc) + ';' + str(current_sww['ordered']))
            current_sww = file_ordered_sww.__next__()
            current_sww_pc = current_sww['product_code']    # product code from next string

        if row['product_code'] == current_sww_pc:
            row['stock'] = str(int(row['stock']) - int(current_sww['ordered']))
            if cur_sww_position < row_in_sww:
                current_sww = file_ordered_sww.__next__()
                current_sww_pc = current_sww['product_code']    # product code from next string
                cur_sww_position += 1

        if row['product_code'] > current_ozon_pc and cur_ozon_position < row_in_ozon:
            current_ozon = file_ordered_ozon.__next__()
            current_ozon_pc = current_ozon['product_code']    # product code from next string
            # cur_ozon_position += 1

        if row['product_code'] == current_ozon_pc:
            row['stock'] = str(int(row['stock']) - int(current_ozon['ozon_ordered']))
            if cur_ozon_position < row_in_ozon:
                current_ozon = file_ordered_ozon.__next__()
                current_ozon_pc = current_ozon['product_code']  # product code from next string
                cur_ozon_position += 1

        # print("276 — current_ozon_st_pc = ", current_ozon_st_pc,
        #       " row['product_code'] = ", row['product_code'],
        #       " cur_ozon_st_position = ", cur_ozon_st_position, " cur_sww_position = ", cur_sww_position,
        #       " row_in_ozon_st = ", row_in_ozon_st)

        while row['product_code'] > current_ozon_st_pc and cur_ozon_st_position < row_in_ozon_st:
            if int(current_ozon_st['ozon_stock']) != 0:     # if present stock in Ozon, but it absent in sww
                ordered_alert.append(str(current_ozon_st_pc) + ';' + str(current_ozon_st['ozon_stock']))
            # print("286 — current_ozon_st_pc", current_ozon_st_pc)
            current_ozon_st = file_st_ozon.__next__()
            current_ozon_st_pc = current_ozon_st['product_code']    # product code from next string
            cur_ozon_st_position += 1
            # print("290 — current_ozon_st_pc", current_ozon_st_pc)
            if row['product_code'] == current_ozon_st_pc:
                break
            # print("293 — cur_ozon_st_position —>", cur_ozon_st_position, " cur_ozon_st_position = ",cur_ozon_st_position)

        # print("287 — current_ozon_st_pc", current_ozon_st_pc, " row['product_code'] = ", row['product_code'])
        if row['product_code'] == current_ozon_st_pc:
            sww_for_compare.append((str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name']))
            if int(row['stock']) != int(current_ozon_st['ozon_stock']):
                sww_to_ozon_syncro.append((str(row['product_code']) + ';' + str(row['stock'])))
            if cur_ozon_st_position < row_in_ozon_st:
                current_ozon_st = file_st_ozon.__next__()
                current_ozon_st_pc = current_ozon_st['product_code']  # product code from next string
                cur_ozon_st_position += 1

        # full sww stock data with decreasing goods quantity
        sww_minused.append(
            str(row['product_code']) + ';' + str(row['stock']) + ';' + row['product_name'])

        sww_position += 1

r_file_o_sww.close()
r_file_o_ozon.close()
r_file.close()

write_sorted(sww_minused, 'sww_minused.csv')
write_sorted(sww_for_compare, 'sww_for_compare.csv')
if len(ordered_alert) > 0:
    write_ozon_ordered(ordered_alert, 'ozon_alert.csv')
if len(ordered_alert_toomuch) > 0:
    write_ordered_sww(ordered_alert_toomuch, 'ordered_alert_toomuch.csv')

write_ozon_ordered(sww_to_ozon_syncro, 'sww_to_ozon_syncro.csv')

# then we are ready to compare goods from sww stock in file_reader
# and ozon stock from ozon_stock.csv

# st_ozon = 'ozon_stock.csv'
# r_file_s_ozon = open(st_ozon, encoding='utf-8')
# file_st_ozon = csv.DictReader(r_file_s_ozon, delimiter=";", quotechar='"')

# is it correct firstly select goods from file_reader?



