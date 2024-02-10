def count_prime(n: int):
    '''
    :param n: int
    :return:
    '''
    count = 0   # Counter to store the number of prime numbers

    # Iterate through numbers up to 'n'
    for num in range(n):
        if num <= 1: # Numbers less that or equal to 1 are not prime so skip
            continue
        if num == 2:
            print(2)
        for i in range(3, num):
            if (num % i) == 0: # If num is divisible by i , it is not prime
                break
            else:
                count += 1
    return count

def check_number_is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    result = True
    for x in range(2, n):
        if n%x == 0:
            result = False
            break
    return result

print(check_number_is_prime(10))
print([x for x in range(20) if check_number_is_prime(x) == True])

# print(count_prime(54))