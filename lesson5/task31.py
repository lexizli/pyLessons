def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(7))
print(fib(8))

# 0 1 1 2 3 5 8 13 21

