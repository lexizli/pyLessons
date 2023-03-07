# Задача 26:
# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

def rec_degree(base, degree):
    if degree == 0:
        return 1
    return base * rec_degree(base, degree - 1)


base = int(input())
degree = int(input())
print(rec_degree(base, degree))