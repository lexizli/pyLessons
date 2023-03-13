# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# almost_square = map((lambda x, y: x * y if (x != y) else 0), orbits)
#
# # maxi = max(almost_square)
#
# print(almost_square)

# print([orbits[i] for i in range(orbits) max(orbits[i][0] * orbits[i][1]) if orbits[i][0] != orbits[i][1]])
# print(orbits[3][0] * orbits[3][1])
#
# newli = []
# for i in orbits:
#     valli = orbits[i][0] * orbits[i][1] if orbits[i][0] != orbits[i][1] else 0
#     newli.append(valli)
#
# print(newli)

def func(li):
    dict = {i[0] * i[1]: i for i in li if i[0] != i[1]}

    return max(dict.items())[1]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]

print(*func(orbits))