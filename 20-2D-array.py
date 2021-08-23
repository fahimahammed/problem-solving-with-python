# 20. Write a program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. 

m = int(input("Enter number of row: "))
n = int(input("Enter number of column: "))

multi_list = [[0 for col in range(n)] for row in range(m)]

for row in range (m):
    for col in range(n):
        multi_list[row][col]=row*col

print(multi_list)