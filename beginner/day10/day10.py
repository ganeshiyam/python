# Functions with outputs
from art import logo_calculator


# More Functions
# def my_function():
# Do this
# Then do this
# Finally do this

# def my_function1(something):
# Do this with something
# Then do this
# Finally do this

def my_function2():
    result = 3 * 2
    return result


output = my_function2()
print(output)


def format_name(f_name, l_name):
    """Take a first name and last name and format it to return the title case version of it"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."  # Multiple Return Values
    # f_name.title()
    # l_name.title()
    # print(f"Your Name is {f_name.title()} {l_name.title()}")
    return f"Your Name is {f_name.title()} {l_name.title()}"


f_n = input("Enter your First name: ")
l_n = input("Enter your Last name: ")
print(format_name(f_n, l_n))


# Exercise - Days in Month

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO: Add more code here 👇
def days_in_month(y, m):
    """Takes the year and month and provides the number of days in that month
    :rtype: int
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and is_leap(y):
        return month_days[m - 1] + 1
    else:
        return month_days[m - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))  # Enter a year
month = int(input("Enter a month: "))  # Enter a month
days = days_in_month(year, month)
print(days)


# DocStrings
# def my_function3():
# """ Doc String of the function with the return object details"""


# Calculator App

# Addition
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo_calculator)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        proceed = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculations.: ")
        if proceed == "y":
            num1 = answer
        elif proceed == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False
            print("Thank you!")


calculator()
