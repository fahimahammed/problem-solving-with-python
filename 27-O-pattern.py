# 27. Write a program to print alphabet pattern O.

n = 5

for row in range(n):
    for col in range(n):
        if ((row == 0 or row == 4) and (col == 1 or col == 2 or col == 3)) or ((row == 1 or row == 2 or row == 3) and ((col == 0 or col == 4))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")