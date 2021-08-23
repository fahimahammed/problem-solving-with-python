# find maximum number from three number

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

if a > b and a > c:
    print(f"{a} is Largest number")
elif b > a and b > c:
    print(f"{b} is Largest number")
else: 
    print(f"{c} is Largest number")