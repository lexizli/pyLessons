# Задача 8: Требуется определить, можно ли от шоколадки
# размером n × m долек # отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

try:
    column = int(input("Введите m: "))
    row = int(input("Введите n: "))
    part = int(input("Введите k: "))
except:
    print("Что-то не то вы ввели, пока!")

if (part % column == 0 or part % row == 0) and part < column * row:
    print("\nТакой кусочек можно отломить")
else:
    print("\nТакой кусочек отломить невозможно")
