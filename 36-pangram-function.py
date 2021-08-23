# 36. Write a function to check whether a string in a pangram or not. NOTE: Pangrams are words or sentences containing every letter of the alphabet at least once.

import string, sys
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("zxcvbnmasdfghjklqwertyuiop"))