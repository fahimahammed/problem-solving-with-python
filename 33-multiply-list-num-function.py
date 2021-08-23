# 33. Write a function to multiply all the numbers in a list.

def mul_list(list):
    total = 1
    for i in list:
        total *= i
    return total

l = (10, 20, 30, 40, 50)
print(mul_list(l))