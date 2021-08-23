# 32. Write a function to reverse a string. 

def rev_string(text):
    rev_str = ""
    if len(text) > 0:
        for i in range(len(text)-1, -1, -1):
            rev_str += text[i]
        return rev_str
    else:
        return "This is empty string."

str1 = input("Enter a string: ")
print(rev_string(str1))
