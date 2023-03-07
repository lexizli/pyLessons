file_codes = open('kodes_till_03_07_2023.csv')
strick_codes = open('strick_till_07_03_2023.csv')

old_product_codes = []
stricks = []

for line in file_codes:
    old_product_codes.append(line.strip().replace('"', '').split(";"))
    # if line1[1] == "475T-FAS-90|52-54_182-188":
    # print(line[0], line[1])

# print(old_product_codes)

for line2 in strick_codes:
    stricks.append(line2.strip().replace('"', '').split(";"))
    # if line3[1] == "475T-FAS-90|52-54_182-188":
    #     print(line3[0], line3[1])

# print(stricks)

new_list = open('new_list.csv', 'w')
delimiter1 = '; "'
delimiter2 = '"; "'
delimiter3 = '"\n'

new_stricks = open('new_stricks.csv', 'w')
for line3 in stricks:
    print(line3)
    new_stricks.write(line3[0] + delimiter1 + line3[1] + delimiter3)
new_stricks.close()

for line in old_product_codes:
    key = line[1]
    print(line[1])
    for line1 in stricks:
        if line1[1] == key:
            print(line, line1)
            new_list.write(line[0] + delimiter1 + line1[0] + delimiter2 + line[1] + delimiter2 + line[2] + delimiter3)

new_list.close()
