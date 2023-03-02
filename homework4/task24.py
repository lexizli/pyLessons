bushes =[4, 1, 3, 2, 7, 9, 11, 8, 6, 5]
# нужно найти максимальную сумму трех любых последовательных элементов массива
# мы считаем массив круговым
# Сначала тупо увеличиваем массив на два элемента
print(bushes)
bushes.append(bushes[0])
bushes.append(bushes[1])
print(bushes)

sum_three = 0

for i in range(len(bushes) - 2):
    sum_three = bushes[i] + bushes[i+1] + bushes[i+2] if bushes[i] + bushes[i+1] + bushes[i+2] > sum_three else sum_three

print(sum_three)


