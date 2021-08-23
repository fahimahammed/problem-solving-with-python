# 18. Write a program to get the fibonacci series between 0 to 50. 

x, y = 0, 1
print(x, end=" ")
while y < 50:
    print (y, end=" ")
    x , y = y , x+y 