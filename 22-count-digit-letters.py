# 22. Write a program to check a string and calculate the number of digits and letters.

s = input("Enter a string: ")
digit = 0
letter = 0

for c in s:
    if c.isdigit():
        digit += 1
    elif c.isalpha():
        letter += 1

print(f"Number of digits: {digit}")
print(f"Number of letters: {letter}")
