# 28. Write a program to construct the following pattern, using nested loop.

n = 5
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print("\n")

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print("\n")