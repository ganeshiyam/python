# Python Functions & Karel
# Functions, Code Blocks , While Loops

# Functions

print("Hello")
num_char = len("Hello")
print(num_char)


# Create my own function
# Define the function using "def" and function name, then wat to do inside the function and finally call the function
# to use


def my_function():
    print("Hello")
    print("Python")


my_function()


# Indentation


def my_function1():
    print("Nice work")


# While Loop

list_of_items = [1, 2]
something_is_true = 0
for item in list_of_items:
    # Do something to each item
    print(item)
for number in range(1, 5):
    print(number)
while something_is_true:
    # Do something repeatedly
    print("True")


def jump():
    print("jump")


num_of_hur = 6
while num_of_hur > 0:
    jump()
    num_of_hur -= 1


def at_goal():
    print("At goal")


while not at_goal():
    jump()

# Exercise - Passing the Maze
