# 37. Write a function that prints out the first n rows of pascal's triangle. 

def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l+r for l, r in zip(trow+y,  y + trow)]
    return n>=1

num = int(input("Enter a number: "))
pascal_triangle(num)