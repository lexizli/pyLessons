def simple(number):
    for i in range(2, number-1):
        # print(number % i)
        if number % i == 0:
            return("No")
    return("Yes!")


for i in range(2,22):
    print(f'{i} -> {simple(i)}')



