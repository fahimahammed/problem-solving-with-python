# 7. Write a python program to print the calendar of a given month and year.

import calendar

month = int (input("Enter the month: "))
year = int (input("Enter the year: "))

print(calendar.month(year, month))
