## simple calculator

def add_num(num1, num2):
    return num1 + num2

def sub_num(num1, num2):
    return num1 - num2

def mul_num(num1, num2):
    return num1 * num2

def div_num(num1, num2):
    return num1 / num2

option = 1

while option != 0:
    print("\n-----------------------")
    print("Chose your option: \n-----------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("0. Exit")
    print("-----------------------")

    option = int(input("Input num that you selected: "))
    if option > 4:
        print("\n\n# Please select the correct option")
    elif option <=4 and option >= 1:
        a = int(input("Enter a number1: "))
        b = int(input("Enter a number2: "))
        if option == 1:
            print(f"Result: {add_num(a, b)}")
        elif option == 2:
            print(f"Result: {sub_num(a, b)}")
        elif option == 3:
            print(f"Result: {div_num(a, b)}")
        else:
            print(f"Result: {mul_num(a, b)}")
