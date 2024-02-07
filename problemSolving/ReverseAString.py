# Reverse a String
# Create a function called reverse_string that takes a string as input and returns a new string with its characters reversed.
# Your function should use only built-in Python tools.

def reverse_string(s: str):
    '''
    :param s: str
    :return: str
    '''
    return s[::-1]

print(reverse_string("Hello"))