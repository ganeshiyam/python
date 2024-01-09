# Printing, String Manipulation, Input Function, Variables

print("Hello World!\n")

# Exercise 1 - Printing
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')\n")

# Exercise 2 - String Manipulation
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("Hello" + " World")
print("New lines can be created with a backslash and n.\n")

# Exercise 3 - Input Function
name = input('What is your name? ')
print(len(name))
print(len(input('What is your name? ')))

# Exercise 4 - Variables
# Write a program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

# Exercise 5 - Band Name Generator

print("Welcome to the Band Name Generator")
city = input("What's name of the city you grew up in?\n")
pets_name = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pets_name)
