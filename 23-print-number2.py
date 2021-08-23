# 23. Write a program that prints all the numbers form 0 to 6 except 2 and 6.

for i in range(0, 7):
    if i == 2 or i == 6:
        continue
    print(i, end=" ")