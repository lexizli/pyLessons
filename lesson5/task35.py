def simple(number):
    for i in range(2, number-1):
        # print(number % i)
        if number % i == 0:
            return("No")
    return("Yes!")


for i in range(2,2222):
    print(f'{i} -> {simple(i)}')

    #
    # def is_simple(num):
    #     if num in [2, 3]:
    #         return True
    #     if num % 2 == 0 or num < 2:
    #         return False
    #     for i in range(3, int(num ** 0.5) + 1, 2):
    #         if num % i == 0:
    #             return False
    #     return True
    #
    #
    # print(is_simple(3))



