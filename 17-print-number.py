# 17. Write a program that prints all the numbers from 0 to 6 except 3 and 6. 
for x in range(1, 7):
    if x == 3 or x == 6:
        continue
    print(x, end=' ')