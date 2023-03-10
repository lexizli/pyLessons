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

from time import time
from random import choices
start = time()

liss = choices(range(3000), k=2000)

# # liss = [1, 2, 3, 5, 8, 15, 23, 38]
#
# liss2 = []
# liss2.append([f'{x}, {x * x}' for x in liss if x % 2 == 0])

#
# def select(f, col):
#     return [f(x) for x in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]

liss2 = map(int, liss)
liss2 = filter(lambda x: x % 2 == 0, liss2)
liss2 = list(map(lambda x: (x, x ** 2), liss2))

print(time() - start)

print(liss)
print(liss2)

