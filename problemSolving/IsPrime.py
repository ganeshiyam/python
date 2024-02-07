def is_prime(number: int):
    '''
    :param number: int
    :return: bool
    '''
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if number % i == 0:
                return False
        return True

print(is_prime(9))