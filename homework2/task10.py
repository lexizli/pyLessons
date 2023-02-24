# Задача 10:
# На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.

import random
try:
    total = int(input("Сколько монет на столе? "))
except:
    print("Вы ввели не число, пока!")

random.seed
coins = []
sum_of_zero = 0
for i in range(total):
    coins.append(random.randint(0, 1))
    sum_of_zero = sum_of_zero + 1 if coins[i] == 0 else sum_of_zero
to_revert = sum_of_zero if total - sum_of_zero > sum_of_zero else total - sum_of_zero
print (f'Нужно перевернуть {to_revert}')
print(coins)


