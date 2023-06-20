# import csv
#
# ordered_ozon = 'ordered_sww_sum.csv'
# r_file_o_ozon = open(ordered_ozon, encoding='utf-8')
# file_ordered_ozon = csv.DictReader(r_file_o_ozon, delimiter=";", quotechar='"')
import csv
from os import path

#
# temp = file_ordered_ozon.__next__()
# print(temp['product_code'])
# print(temp['ordered'])
#
# print(file_ordered_ozon.__next__()['product_code'])
# print(file_ordered_ozon.__next__())
# print(file_ordered_ozon.__next__())
#
# with open(ordered_ozon, "r") as f:
#     reader = csv.reader(f)
#     row_count = sum(1 for row in reader)
#
# print(row_count)

# while True:
#     try:
#         print(file_ordered_ozon.__next__())
#     except StopIteration:
#         break

# filename = 'order_items_for_syncro.csv'
#
# if not path.exists(filename):
#     exit('File order_items_for_syncro.csv not exists')
# else:
#     r_file = open(filename, encoding='utf-8')
#     file_temp = r_file.readlines()
#     r_file.close()
#
# print(len(file_temp))

filename = 'products_stock_tikhvin.csv'

if not path.exists(filename):
    exit('File stock_out.csv not exists')
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.readlines()
    r_file.close()

pst_head_and_sorted = []

for line in file_temp:
    line = line.replace('"', '')
    kwo = line.split(';')
    if len(kwo[3]) == 13 and kwo[3][0] == "2":
        pst_head_and_sorted.append(str(kwo[3]) + ';' + str(kwo[4]) + ';' + str(kwo[5].strip()))

    #     print(kwo[3])

pst_head_and_sorted.sort()

for line in pst_head_and_sorted:
    print(line)