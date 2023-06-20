"""
Preparing exported from Internet-shop sww.com.ru file of stock
for using in synchronisation
2023/05/22
© Aleksei Litvinov

input file — product_stock_tikhvin.csv
output file — stock_tikhvin_prepared.csv
"""
import os
from os import path


def tikhvin_stock_prepare():
    filename = 'input/products_stock_tikhvin.csv'

    path = os.path.join(os.getcwd(), filename)

    if not os.path.exists(path):
        exit('File ./input/products_stock_tikhvin.csv not exists')
    else:
        r_file = open(filename, encoding='utf-8')
        file_temp = r_file.readlines()
        r_file.close()

    pst_head_and_sorted = []

    for line in file_temp:
        line = line.replace('"', '')
        kwo = line.split(';')
        if len(kwo[3]) == 13 and kwo[3][0] == "2":
            pst_head_and_sorted.append(str(kwo[3]) + ';' + str(kwo[5].strip()) + ';' + str(kwo[4]))
        # select product code (started from "2"), stock and product name for output in ready for synchronisation file

    pst_head_and_sorted.sort()

    if len(pst_head_and_sorted) > 0:
        with open('./wrk/stock_tikhvin_prepared.csv', 'w', encoding='utf-8') as fe:
            fe.write('product_code;stock;product_name\n')
            for i in range(len(pst_head_and_sorted)): fe.write(pst_head_and_sorted[i] + '\n')
        fe.close()
