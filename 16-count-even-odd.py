# 16. Write a program to count the number of even and odd numbers from the series of numbers. 

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

count_even = 0
count_odd = 0

for i in numbers:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Number of even numbers: {count_even}")
print(f"Number of odd numbers: {count_odd}")