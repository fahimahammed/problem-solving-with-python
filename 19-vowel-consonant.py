# 19. Write a program to check whether an alphabet is a vowel or consonant.

letter = input("Enter a letter: ")

vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

if letter in vowel:
    print("Vowel")
else:
    print("Consonant")
