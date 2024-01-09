# Python Loops
# Using loops with Python lists

# For Loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)  # Goes inside the loop prints 3 times
print(fruits)  # prints outside the loop only once

# Exercise 1-  Average Height

print("Average Student Height")

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(sum(student_heights))
print(len(student_heights))
student_ave_height = 0
num_of_students = 0
for student in student_heights:
    num_of_students += 1
student_cumulative_height = 0
for student in student_heights:
    student_cumulative_height += student

student_ave_height = student_cumulative_height / num_of_students
print(f"Student Average Height: {round(student_ave_height)}")

# Exercise 2 - High Score
# You are going to write a program that calculates the highest score from a List of scores.
print("High Score")

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
print(max(student_scores))
print(min(student_scores))
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

# For loops & range() function

for number in range(1, 10, 3):  # Increase the range by 3
    print(number)
total = 0
for number in range(1, 101):
    total += number
print(total)

# Exercise 3 - Adding Even Numbers
print("Adding even numbers")
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
total1 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total1 += number
print(total1)

# Exercise 4 - FizzBuzz

'''
You are going to write a program that automatically prints the solution to the FizzBuzz game.
Your program should print each number from 1 to 100 in turn.
When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)

# PyPassword Generator

print("Welcome to PyPassword Generator!")
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
how_many_letters = int(input("How many letters would you like in your password? \n"))
how_many_symbols = int(input("How many symbols would you like? \n"))
how_many_numbers = int(input("How many numbers would you like? \n"))
total_psd_length = how_many_letters + how_many_symbols + how_many_numbers
password = ""

# Easy Method

for letter in range(1, how_many_letters + 1):
    random_letter = random.randint(1, len(letters))  # random.choice(letters)
    print(random_letter)
    password += letters[random_letter]
for symbol in range(1, how_many_symbols + 1):
    random_symbol = random.randint(1, len(symbols))  # random.choice(symbols)
    print(random_symbol)
    password += symbols[random_symbol]
for number in range(1, how_many_numbers + 1):
    random_number = random.randint(1, len(numbers))  # random.choice(numbers)
    print(random_number)
    password += numbers[random_number]

print(password)

# Hard level
password_list = []
for letter in range(1, how_many_letters + 1):
    random_number = random.randint(1, len(letters))  # random.choice(letters)
    password_list.append(letters[random_number])
for symbol in range(1, how_many_symbols + 1):
    random_number = random.randint(1, len(symbols))  # random.choice(symbols)
    password_list.append(symbols[random_number])
for number in range(1, how_many_numbers + 1):
    random_number = random.randint(1, len(numbers))  # random.choice(numbers)
    password_list.append(numbers[random_number])
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += random.choice(password_list)

print(f"Here is your password: {password}")
