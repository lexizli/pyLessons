def reorder(number, step=1, val1=0):
    if step == number:
        val1 = input("Введи число: ")
        print(val1, end=" ")
    else:
        val1 = input(f"Введи число: ")
        reorder(number,step+1,val1)
        print(val1, end=" ")


nums = int(input("Введи количество элементов: "))
reorder(nums)
