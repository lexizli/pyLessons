# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

try:
    number = int(input("Введите целое число: "))
except:
    print("Это было не число, пока!")

if number > 0:
    factorial = number
    while number > 1:
        number -= 1
        factorial *= number
    print(factorial)
else:
    print("Это число не больше нуля, пока!")