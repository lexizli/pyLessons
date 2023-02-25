# Задача №19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг циклический) на K элементов вправо,
# K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

counter = int(input('Сколько элементов списка вы планируете ввести? '))

numbers = []
for i in range(counter):
    numbers.append(int(input('введите очередное число: ')))

shift = int(input('На сколько элементов сдвинуть список? '))

if shift > counter:
    shift = shift % counter

print(shift)
print(counter)
print(numbers)
print(numbers[0:(counter - shift)])
print(numbers[(counter - shift):(counter)])

for i in range(shift):
    numbers.insert(0, numbers.pop(-1))


print(numbers)
