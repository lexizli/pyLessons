# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

number = int(input("Введите количество элементов списка: "))
numbers_list = []
for i in range(number):
    numbers_list.append(int(input()))
value_to_find = int(input("Введите число, которое я буду искать: "))
print(numbers_list)
print(len([value for value in numbers_list if value == value_to_find]))

