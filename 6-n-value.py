# 6. Write a python program that accepts an integer (n) and computes the value of n+nn+nnn.

a = int(input("Enter num: "))

n = int ("%s"%a)
n2 = int ("%s%s"%(a,a))
n3 = int ("%s%s%s"%(a,a,a))

print(n+n2+n3)
