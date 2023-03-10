count1 = int(input('Сколько элементов будет в первом массиве? —> '))
list1 = []
for _ in range(count1):
    list1.append(int(input('\tэлемент массива —> ')))

count_1 = 0

# for i in range(1, count1 - 1):
#     if list1[i] == max(list1[i - 1:i + 2]):
#         count_1 += 1

print(len([i for i in range(1, count1 - 1) if list1[i] == max(list1[i - 1:i + 2])]))

print(len([i for i in range(1, count1 - 1) if list1[i-1] < list1[i] > list1[i + 1]]))

