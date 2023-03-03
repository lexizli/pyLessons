counter = int(input('Сколько оценок всего? '))

numbers = []
for i in range(counter):
    numbers.append(int(input('введите еще оценку: ')))

numbers_max = max(list(numbers));
number_min = min(list(numbers));

for i in range(counter):
    numbers[i] = number_min if numbers[i] == numbers_max else numbers[i]

print(numbers)