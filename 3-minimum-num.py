# find minimum number of three numbers 

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
c = int(input("Enter num3: "))

if a < b and a < c:
    print(f"{a} is smallest number")
elif b < c and b < a:
    print(f"{b} is smallest number")
else: 
    print(f"{c} is smallest number")