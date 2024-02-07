# Basic String Manipulation
# Write a function called greet that takes two arguments: name (a string) and age (an integer).
# The function should return a string message in the format "Hello, [name]! You are [age] years old."

def greet(name: str, age: int) -> str:
    '''
    :param name: str
    :param age: int
    :return: str
    '''
    return f"Hello, {name}! You are {age} year old."

print(greet('Twisha', 9))
print(greet('Shastik', 1))
