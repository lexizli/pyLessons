import os

filename = 'input/products_stock_tikhvin.csv'

path = os.path.join(os.getcwd(), filename)

if not os.path.exists(path):
    exit('File ./input/products_stock_tikhvin.csv not exists')
else:
    r_file = open(filename, encoding='utf-8')
    file_temp = r_file.readlines()
    r_file.close()