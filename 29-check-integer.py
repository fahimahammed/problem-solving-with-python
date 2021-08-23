# 29. Write a program to check a string represent an integer or not.

text = input("Enter a string: ")
text = text.strip()
if len(text)<1:
    print("Input a valid text.")
else:
    if (text[0] in "+-") and all(text[i] in "0123456789" for i in range(1, len(text))):
        print("This String is an integer")
    elif all(text[i] in "0123456789" for i in range(len(text))):
        print("This String is an integer")
