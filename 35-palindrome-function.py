# 35. Write a function that checks whether a passed string in palindrome or not. NOTE: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def check_palindrome(word):
    left = 0
    right = len(word) -1

    while left < right:
        if word[left] == word[right]:
            return "It is palindrome"
        else:
            return "It is not palindrome"
    right -= 1
    left += 1

word = input("Enter a string/word:")
print(check_palindrome(word))