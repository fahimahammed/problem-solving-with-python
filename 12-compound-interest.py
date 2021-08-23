# 12. Write a python program to calculate Compound Interest.

def compoundInterest (principle, rate, time):
    return principle * (pow((1+rate), time))

p = float(input("Enter the Principal amount: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the Time: "))

interest = compoundInterest(p, r, t) - p
print(f"Compound Interest: {interest}")