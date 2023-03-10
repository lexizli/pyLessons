count1 = int(input('Сколько элементов будет в первом массиве? —> '))
list1 = []
for _ in range(count1):
    list1.append(int(input('\tэлемент массива —> ')))
count2 = int(input('Сколько элементов dj втором массиве? —> '))
list2 = []
for _ in range(count2):
    list2.append(int(input('\tэлемент массива —> ')))

print([x for x in list1 if x not in (list2)])
