# Write a Python program to swap two variables.
# Input two variables
a = input("Enter the value of the first variable: ")
b = input("Enter the value of the second variable: ")
# Display the original values
print(f"Original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")


# Write a Python program to swap two variables without temp variable.
# Input two variables
c = input("Enter the value of the first variable: ")
d = input("Enter the value of the second variable: ")
# Display the original values
print(f"Original values: c = {c}, d = {d}")
# Swapping without a temporary variable
c, d = d, c
# Display the swapped values
print(f"Swapped values: c = {c}, d = {d}")

