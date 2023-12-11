# Write a Python program to do arithmetical operations addition and division.

# Addition
num1 = float(input("Enter the first number for Addition: "))
num2 = float(input("Enter the second number for Addition: "))
sum_result = num1 + num2
print(f"Addition: {num1} + {num2} = {sum_result}")

# Subtraction
num3 = float(input("Enter the first number for Subtraction: "))
num4 = float(input("Enter the second number for Subtraction: "))
subtraction_result = num3 - num4
print(f"Subtraction: {num3} - {num4} = {subtraction_result}")

# Multiplication
num5 = float(input("Enter the first number for Multiplication: "))
num6 = float(input("Enter the second number for Multiplication: "))
multiplication_result = num5 * num6
print(f"Multiplication: {num5} * {num6} = {multiplication_result}")

# Division
num7 = float(input("Enter the dividend for Division: "))
num8 = float(input("Enter the divisor number for Division: "))
if num8 == 0:
    print("Error: Division by zero is not allowed.")
else:
    division_result = num7 / num8
    print(f"Division: {num7} / {num8} = {division_result}")

# Power
num9 = float(input("Enter the first number for Power: "))
num10 = float(input("Enter the second number for Power: "))
power_result = num9 ** num10
print(f"Power: {num9} ** {num10} = {power_result}")