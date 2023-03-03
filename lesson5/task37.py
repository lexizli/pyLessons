# def reorder(number, step=1, val1=0):
#     if step == number:
#         val1 = input("Введи символ: ")
#         print(val1, end=" ")
#     else:
#         val1 = input(f"Введи символ: ")
#         reorder(number,step+1,val1)
#         print(val1, end=" ")

def reorder(number):
    if number == 0:
        return ""
    strochechka = input()
    return reorder(number - 1) + strochechka

nums = int(input("Введи количество элементов: "))
print(reorder(nums))

# print(n[::-1])