# 13. Write a program to convert given number of days in terms of Years, Weeks and Days.

def find(num_of_days):
    year = int(num_of_days / 365)
    week = int((num_of_days % 365)/7)
    days = int((num_of_days % 365) % 7)
    print(f"Year: {year} \nWeek: {week} \nDays: {days}")

days = int(input("Enter the number of days: "))
find(days)