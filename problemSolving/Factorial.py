# Calculate the Factorial
# Write a function called factorial that takes a positive integer as an argument and returns its factorial.

def factorial(num: int):
    '''
    :param num: int
    :return:
    '''
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

print(factorial(6))
print(factorial(8))