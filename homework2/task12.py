# Задача 12:
# Петя задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math

try:
    mult = int(input("Произведение чисел? "))
    sum = int(input("Сумма чисел? "))
except:
    print("Вы ввели не числа, пока!")

if sum > mult:
    print("Вы ввели неверные числа, пока!")
else:
    discriminant = sum * sum - 4 * mult
    if discriminant < 0 or math.sqrt(discriminant) != math.isqrt(discriminant):
        print("Решения в положительных целых числах нет, пока!")
    else:
        print(f'Задуманные числа {(sum + math.isqrt(discriminant))//2} и {(sum - math.isqrt(discriminant))//2}')