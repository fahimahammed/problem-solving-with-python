# 11. Write a python program that prints the perimeter of a rectangle to take its height and width as input.

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

area = width * height
perimeter = 2 * (width + height)

print("The area of the rectangle: {0: 0.2f}".format(area))
print("The perimeter of the rectangle: {0: 0.2f}".format(perimeter))