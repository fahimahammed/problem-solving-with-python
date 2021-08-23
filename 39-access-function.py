# 39. Write a program to access a function inside a function.

def test(a):
    def add(b):
        return a + b
    return add

func = test(4)
print(func(3))