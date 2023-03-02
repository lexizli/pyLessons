# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

instr = input().split()
# values = 1instr.split()

# print([instr[i].value()+sum(instr[i] == instr[i - 1]) for i in range(len(instr))])

newlist = [instr[i] for i in range(len(instr)) if instr[i] == instr[i -1]]
# newlist = [x+str(sum(instr[x] == instr[x - 1])) for x in instr]
print(newlist)

