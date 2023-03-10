# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:
# a(n) = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
#
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
from time import time

first = int(input('First value in progression? —> '))
diff = int(input('Difference in progression? —> '))
numb = int(input('Values number in progression? —> '))

start = time()


progression = [first + x * diff for x in range(numb)]    # 1 000 000 values for 0.08577394485473633

# progression = [first + (x - 1) * diff for x in range(1, numb+1)]    # 1 000 000 values for 0.09972500801086426


# variance 2 — # 1 000 000 values for 0.10433220863342285
# progression = []
# progression.append([first + (x - 1) * diff for x in range(1, numb+1)])

# variance 3 — # 1 000 000 values for 0.14879727363586426
# progression = []
# for x in range(1, numb+1):
#     progression.append(first + (x - 1) * diff)

print(time() - start)
print(progression)