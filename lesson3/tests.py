#
# squares = []
# for i in range(10):
#     squares.append(i * i)
#
# quads = map(lambda num: num ** 2, squares)
#
# print(list(quads))

sentence = 'The rocket, who was named Ted, came back'


def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels


# print([i for i in sentence if is_consonant(i)])
print([i for i in sentence if i.isalpha() and i not in 'aeiou'])