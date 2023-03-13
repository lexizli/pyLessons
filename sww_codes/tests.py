# lis = []
# lis.append([x for x in range(1, 11) if x % 2 == 0])
# lis.append([x for x in range(11, 18) if x % 2 != 0])
# lis.append([x for x in range(19, 29) if x % 2 == 0])
# lis.append([x for x in range(29, 36) if x % 2 != 0])
#
# flat = [x for i in lis for x in i]
#
# sector = int(input())
# if sector > 36 or sector < 0:
#     print('ошибка ввода')
# elif sector == 0:
#     print('зеленый')
# elif sector in flat:
#     print('черный')
# else:
#     print('красный')

#
# a1, b1, a2, b2 = int(input('a1 ')), int(input('b1 ')), int(input('a2 ')), int(input('b1 '))
#
# if b1 > a1 > b2 > a2 or a2 < a1:
#     a1, b1, a2, b2 = a2, b2, a1, b1
#
# print(a1, b1, a2, b2)
#
# if a2 > b1:
#     print('пустое множество')
# elif a2 == b1:
#     print(a2)
# elif b2 < b1:
#     print(a2, b2)
# else:
#     print(a2, b1)
#

from math import *

a, b, c = float(input()), float(input()), float(input())
des = b * b - 4 * a * c
if des < 0:
    print("Нет корней")
elif des == 0:
    print(-b /(2 * a))
else:
    print((-b + des ** 0.5 )/(2 * a))
    print((-b - des ** 0.5 )/(2 * a))



