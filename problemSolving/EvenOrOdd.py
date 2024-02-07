# Even or Odd
# Write a function called is_even that takes a number as an argument and returns True if it's even, and False otherwise

def is_even(num: int):
    '''
    :param num: int
    :return: bool
    '''
    return num % 2 == 0

print(is_even(3))
print(is_even(44))