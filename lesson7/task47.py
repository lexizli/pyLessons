# Задача №47
#
# transormed_values = []
# transformation = transormed_values.append(x)
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
transormed_values = list(map(lambda x: x, values))
print(transormed_values)