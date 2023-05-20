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

fname = 'ozon_stock.csv'
r_file_s_ozon = open(fname, encoding='utf-8')
ozon_stock = csv.DictReader(r_file_s_ozon, delimiter=";", quotechar='"')
# print(ozon_stock.line_num)
# print(ozon_stock.__sizeof__())
#
# numline = len(r_file_s_ozon.readlines())
# print(numline)

test = ozon_stock.__next__()
print(test['product_code'])

for i in range(29):
    test = ozon_stock.__next__()
    print(test)