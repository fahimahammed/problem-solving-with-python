# 31. Write a function to find the Max of three numbers.

def max_of_two(a , b):
    if a > b:
        return a
    else: 
        return b

def max_of_three(a , b, c):
    return max_of_two(a, max_of_two(b, c))

a = int(input("Enter a num1: "))
b = int(input("Enter a num2: "))
c = int(input("Enter a num3: "))

print(f"Max Num: {max_of_three(a, b, c)}")