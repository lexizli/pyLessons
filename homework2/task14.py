# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

try:
    total = int(input("Введи целое положительное число "))
except:
    print("Вы ввели не число, пока!")

if total <= 0:
    print('Для чисел меньше единицы решения нет')
else:
    degree = 1
    while degree < total:
        print(degree, end = ' ')
        degree *= 2
