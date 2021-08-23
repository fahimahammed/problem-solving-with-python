# 24. Write a program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i = 0, 1, ....., m-1 and j = 0, 1, ......, n-1 

m = int(input("Input number of row: "))
n = int(input("Number of column: "))

multi_list = [ [0 for col in range(n)] for row in range(m)]

for row in range(m):
    for col in range(n):
        multi_list[row][col] = row*col
print(multi_list)