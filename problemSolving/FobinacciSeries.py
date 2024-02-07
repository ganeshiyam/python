# Fibonacci Series
# Write a program that generates the Fibonacci series up to a given number 'n'.
# fibonacci(0) -> []
# fibonacci(10) -> [0, 1, 1, 2, 3, 5, 8]
# fibonacci(23) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n: int):
    '''
    :param n: int
    :return: int
    '''
    num = 2
    n1, n2 = 0, 1
    fib_series = [0, 1]
    if n == 0:
        fib_series = []
    elif n == 1:
        fib_series = [n1, n2]
    else:
        while num <= n:
            nth = n1 + n2
            fib_series.append(nth)
            n1 = n2
            n2 = nth
            num += 1

    return fib_series

print(fibonacci(10))