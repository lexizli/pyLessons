counter_1 = int(input('Сколько элементов первого списка вы планируете ввести? '))
counter_2 = int(input('Сколько элементов второго списка вы планируете ввести? '))

numbers_1 = []
for i in range(counter_1):
    numbers_1.append(int(input('введите очередное число первого списка: ')))
numbers_2 = []
for i in range(counter_2):
    numbers_2.append(int(input('введите очередное число второго списка: ')))

print('Числа, которые нашлись в первом списке: ' + str(sorted(set(numbers_1))))
print('Числа, которые нашлись во втором списке: ' + str(sorted(set(numbers_1))))
