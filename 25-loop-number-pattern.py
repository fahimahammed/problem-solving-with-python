# 25. Write a program to construct the following pattern, using nested loop number.

n = int(input("Enter row number of pattern: "))

for i in range(n):
    print(str(i)*i)
    