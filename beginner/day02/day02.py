# Data Types, Numbers, Operations, Type Conversion, f-Strings

# Primitive Data Types
# String Integers Floats & Boolean
print(len("Hello"))  # String
print("Hello"[0])  # String Indices
print("123" + "345")  # String Concatenation
print(123 + 345)  # Integers
print(3.14159)  # Floats

# Type Error, Type Checking, Type conversion
num_char = len(input("What is your name? "))
print(type(num_char))
print("Your name has " + str(num_char) + " characters.\n")

# Exercise - Data type
# Write a program that adds the digits in a 2-digit number. e.g if the input was 35, then the output is 8
two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
sum_of_two_digit_numbers = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum_of_two_digit_numbers)

# Mathematical Operations  +, -, *, /
# "PEMDASLR - (), **, * /, + -
print("\nMathematical Operations")
print(3 + 5)
print(7 - 4)
print(4 * 5)
print(6 / 3)
print(2 ** 3)
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Exercise - BMI Index Calculator
# BMI = Weight(kg)/Height**2(m**2)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2  # Regular division
bmi_floor_division = int(weight) // float(height) ** 2  # Floor Division
print(int(bmi))
print(round(bmi))
print(bmi_floor_division)

# Round of values, Floor Division,
print("\n")
print(type(8 / 3))
print(type(8 // 3))
result = 4 / 2  # 4/2 = 2
result /= 2  # 2/2
print(result)
score = 0
score += 2
print(score)
score -= 1
print(score)
score *= 2
print(score)
score /= 3
print(score)

# F - String
print("F- String \n")
score1 = 0
height1 = 1.8
isWinning = True
# f-string
print(f"your score is {score1}, your height is {height1}, you are winning is {isWinning}")

# Exercise 3 - Life in weeks
print("\nLife in Weeks")
age = input("What is your current age? ")
bal_to_live = 90 - int(age)
days = bal_to_live * 365
weeks = bal_to_live * 52
months = bal_to_live * 12
print(f"You have {days} days, {weeks} weeks, and {months} months left.\n")

name = input("What is your name?")
print(f"Hello, {name}")
print("Hello, " + name)
age = 23
print(f"You are {age} years old")
print("You are" + str(age) + "years old")

# Project - Tip Calculator

print("\nTip Calculator")
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")
total_tip = (float(bill) * int(tip)) / 100
total_amt_with_tip = float(bill) + float(total_tip)
bill_per_person = float(total_amt_with_tip) / int(split)
print(f"Each person should pay: ${round(bill_per_person, 2)}")
