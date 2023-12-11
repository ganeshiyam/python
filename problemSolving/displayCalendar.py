# Write a Python program to display calendar.

import calendar

year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

cal = calendar.month(year, month)
print(cal)
