# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# # count1 = int(input('Сколько элементов будет в первом массиве? —> '))
# list1 =  [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3, 3, 3]
# for _ in range(count1):
#     list1.append(int(input('\tэлемент массива —> ')))

from time import time
from random import choices
start = time()

list1 = choices(range(3000), k=2000)

vals = set(list1)

# print(set([list1.count(x) for x in vals if list1.count(x) % 2 == 0]))

dic = {}.fromkeys(list1,0)
for i in list1:
    dic[i] += 1

print(sum([i //2 for i in dic.values() if not i % 2]))

print(time() - start)


# li =  [1, 2, 3, 4, 2, 3, 4, 3, 5, 6, 5, 3, 3, 3]
# решение от Гаи не катит
# sum = 0
# for i in li:
#     if li.count(i) > 1:
#         if li.count(i) % 2 != 0:
#             sum += (li.count(i) - 1) / 4
#             li.pop(i)
#         else:
#             sum += li.count(i) / 4
#         print(f'i = {li.count(i) / 4}, sum = {sum}')
