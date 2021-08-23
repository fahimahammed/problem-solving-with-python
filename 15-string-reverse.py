# 15. Write a program that accepts a word the user and reverse it. 
word = input("Enter a string/word: ")

for i in range(len(word)-1, -1, -1):
    print (word[i], end="")


# alternative

# word = input("Enter a string/word: ")

# rev_word = word[::-1]
# print (rev_word)
