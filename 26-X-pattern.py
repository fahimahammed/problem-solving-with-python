# 26. Write a program to print alphabet pattern X.

n = 5


for row in range(0, n):
    for col in range(0, n):
        if ((row == 0 or row == 4) and (col == 0 or col == 4)) or ((row == 1 or row == 3) and (col == 1 or col == 3)) or (row == col):
            print ("#", end=" ")
        else:
            print(" ", end=" ")
    print("\n")