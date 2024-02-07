def count_prime(n: int):
    '''
    :param n: int
    :return:
    '''
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        for i in range(2, n):
            if n % i == 0:
                i += 1
            else:
                print(i)

print(count_prime(10))