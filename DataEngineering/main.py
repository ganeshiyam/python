print('Hello World!')

# Data Types
string = "Hello Python"
integer = 4
integer_ = float(4)
float_ = 3.13
float_1 = int(3.13)
boolean = True  # False
boolean_ = 3 < 2    # 3 > 2, 3 == 3,

operation = 3 + 4   # 3 - 4, 12 / 4, 13 // 4, 3 * 4, "12" + "3"

variable_of_interest = string[0]  # string, string[0]
print(variable_of_interest, type(variable_of_interest))

# Basic String Operations
# Concatenation: Joining two or more strings together using the '+' operator.
# Indexing: Accessing individual characters in a string using square brackets [] and indices.
# Slicing: Extracting substrings from a string using the colon (:) operator and specifying start and end indices.
# Length: Determining the length of a string using the len() function
print(string[0:3] + string[4:8], string[1], string[2:5], len(string))

# String Methods
# split(): Splits a string into a list of substrings based on a specified delimiter.
# join(): Joins a list of strings into a single string using a specified delimiter.
# strip(): Removes leading and trailing whitespace characters from a string.
# replace(): Replaces occurrences of a substring within a string with another substring.
# lower() and upper(): Converts a string to lowercase or uppercase, respectively.

print(string.split(' '))

# Formatting Strings
# Python offers multiple approaches for formatting strings, enabling us to create dynamic and visually appealing output.
# Here are two popular methods:
# String Interpolation: Using the 'f' prefix before a string and embedding expressions within curly braces {} to dynamically insert values into the string.
# format(): A versatile method that allows for more complex string formatting by using placeholders and positional or keyword arguments.


# Regular Expressions
# Regular expressions provide a powerful and flexible way to search, match, and manipulate strings based on specific patterns.
# Python's built-in re module offers comprehensive support for regular expressions. Some common operations include:
# Pattern matching using metacharacters and quantifiers.
# Search and substitution using functions like re.search(), re.match(), and re.sub().
# Splitting strings based on complex patterns using re.split().


# Working with Unicode and Encoding
# Python's robust string handling capabilities extend to working with Unicode characters and different encodings.
# Understanding how to handle Unicode data and encode/decode strings is essential for dealing with diverse textual content.
# Unicode representation and escape sequences.
# Encoding and decoding strings using different encodings such as UTF-8, UTF-16, etc.
# Detecting and handling encoding errors.

# Basic Integer Operations
# Let's start with the essentials. In Python, integers are whole numbers without decimal points.
# We'll explore some fundamental integer operations that will serve as building blocks for more complex calculations:
# Addition (+): Combining two integers to obtain their sum.
# Subtraction (-): Finding the difference between two integers.
# Multiplication (*): Performing multiplication of two integers.
# Division (/): Obtaining the quotient (result of division) of two integers.
# Modulo (%): Calculating the remainder of integer division.

# Math Module
# Python provides the math module, which offers a wide range of mathematical functions and constants.
# Some useful functions for integer manipulation include:
# math.sqrt(): Finding the square root of an integer.
# math.pow(): Raising an integer to a specific power.
# math.floor() and math.ceil(): Obtaining the floor and ceiling values of an integer, respectively.
# math.factorial(): Calculating the factorial of an integer.

# Number Conversion
# Python provides functions to convert integers between different number systems:
# bin(): Converting an integer to a binary string.
# oct(): Converting an integer to an octal string.
# hex(): Converting an integer to a hexadecimal string.
# int(): Converting a string representation of an integer to an actual integer.

# Random Number Generation
# The random module in Python allows us to generate random integers. Some commonly used functions include:
# random.randint(): Generating a random integer within a specified range.
# random.choice(): Selecting a random element from a list of integers.

# Conditional Statements
x = 1
if x > 1:
    print("X is bigger than 1")
elif x == 1:
    print("X is equal to 1")
else:
    print("X is smaller than 1")


# List
lst = [1, 2, 3, 4, 5]
lst1 = [7, 8, 9]
lst2 = ['a', 'ab', 'cd', 'abcd']
lst3 = [[1, 2, 3], ['a', 'b', 'c'], [1.2, 2.3, 3.4]]
el = lst[1]     # [-1]
el1 = lst[1:3]  # Subset
el2 = lst[::-1] # Reverse the list
el3 = lst[::-2]
lst.append(6)
lst.insert(0, 7)
lst.extend(lst1)
el4 = lst.index(7)
el5 = lst.count(7)
lst.remove(7)
lst.pop(8)  # pop()
squared = [num ** 2 for num in lst if num % 2 == 0]
evens = [num for num in range(1, 10) if num % 2 == 0]
print(el, el1, el2, el3, lst, el4, el5, len(lst), sum(lst), sorted(lst2), squared, evens, min(lst), max(lst), lst3[1], lst3[2][2])

# List vs. Other Data Structures
# When working with collections of data in Python, it's essential to understand the differences between lists and other data structures.
# Here are a couple of comparisons:
# Comparison with arrays: While arrays are fixed in size and require the NumPy library, lists in Python are dynamic and more flexible for handling collections of elements.
# Comparison with tuples: Tuples are similar to lists but are immutable, meaning they cannot be modified after creation.
# Lists, on the other hand, are mutable and allow for modifications.

# Functions

def square(x: int):
    '''
    :param x: int
    :return: int returns square of x
    '''
    y = x ** 2
    return y

print(square(6))

def pow(x, times):
    '''
    :param x:
    :param times:
    :return:
    '''
    return x ** times

print(pow(3, 3))

assert pow(3, 2) == square(3), "There is a mistake with the function"
assert pow(4, 2) == square(4), "There is a mistake with the function"
print("Success")

def greet(name: str, age: int) -> str:
    '''
    :param name:
    :param age:
    :return:
    '''
    m = print(f"Hello, {name}! You are {age} years old.")
    return m

print(greet('Alice', 23))

def is_even(num):
    # Do some checks with num
    return num % 2 == 0

print(is_even(5))

# Loops
for i in lst:
    print(i)

for i in range(1, 8):
    print(i)

counter = 0
while counter < len(lst):
    print(lst[counter])
    counter += 1

number_to_find = 8
for i in lst:
    if i == number_to_find:
        print("Number is found.")
        break
else:
    print("Element not found!")

# Tuples
tup = (1, 2, 3, 4, 5)
print(tup[1])
tup += (6, 7, 8, 9)
print(tup)

# Sets
# Creating Sets
# To create a set in Python, you can use curly braces {} or the built-in set() constructor.

# Using curly braces
my_set = {1, 2, 3, 4}

# Using the set() constructor
another_set = set([4, 5, 6, 7])

print(my_set, another_set)

# Unique Elements
# One of the primary features of sets is that they can only contain unique elements. If you attempt to add duplicates,
# they will be ignored:

unique_set = {1, 2, 3, 3, 4, 4, 5}
print(unique_set)  # Output: {1, 2, 3, 4, 5}

# Basic Operations
# Sets support various operations that come in handy when dealing with unique collections.
# Some common operations include union, intersection, difference, and symmetric difference:

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_result = set_a | set_b  # or use set_a.union(set_b)
print(union_result)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_result = set_a & set_b  # or use set_a.intersection(set_b)
print(intersection_result)  # Output: {3}

# Difference
difference_result = set_a - set_b  # or use set_a.difference(set_b)
print(difference_result)  # Output: {1, 2}

# Symmetric Difference
symmetric_difference_result = set_a ^ set_b  # or use set_a.symmetric_difference(set_b)
print(symmetric_difference_result)  # Output: {1, 2, 4, 5}

# Set Methods
# Python sets come with a range of useful methods to modify, add, or remove elements.
# Some important methods include add(), remove(), discard(), and clear():

my_set = {1, 2, 3}

my_set.add(4)  # Add element 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}

my_set.remove(2)  # Remove element 2 from the set
print(my_set)  # Output: {1, 3, 4}

my_set.discard(3)  # Remove element 3 from the set using discard
print(my_set)  # Output: {1, 4}

my_set.clear()  # Clear all elements from the set
print(my_set)  # Output: set()

# Membership and Length
# You can check for the presence of an element in a set using the in keyword.
# The len() function gives you the number of elements in a set:

my_set = {1, 2, 3, 4}

print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False

print(len(my_set))  # Output: 4

# OOP (Object Oriented Programming)
# OOP is a programming paradigm that revolves around the concept of objects.
# An object is a self contained unit that encapsulates data and behavior related to the data.
# In Python everything is a object, including Int, Str and even functions.


