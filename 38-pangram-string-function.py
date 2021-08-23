# 38. Write a function to create and print a list where the values are sequence of numbers between 1 and 30 (both included). 

import string, sys
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

text = input("Enter a string: ")
print(ispangram(text))