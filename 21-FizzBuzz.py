# 21. Write a program which iterates the integers form 1 to 50. For multiples of three print Fizz instead of the number and form the multiples of five print Buzz. For numbers which are multiples of  both three and five print FizzBuzz.

for i in range (1, 51):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    print (i)
