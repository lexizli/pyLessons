# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

counter = int(input('Сколько элементов списка вы планируете ввести? '))

numbers = []
for i in range(counter):
    numbers.append(int(input('введите очередное число: ')))

print(numbers)
num_values = len(set(numbers))
print(num_values)