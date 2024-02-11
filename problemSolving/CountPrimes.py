def count_prime(n: int):
    """
    :param n: int
    :return:
    """
    count = 0  # Counter to store the number of prime numbers

    # Iterate through numbers up to 'n'
    for num in range(n):
        if num <= 1:  # Numbers less that or equal to 1 are not prime so skip
            continue
        if num == 2:
            print(2)
        for i in range(3, num):
            if (num % i) == 0:  # If num is divisible by i , it is not prime
                break
            else:
                count += 1
    return count


print(count_prime(10))
print(count_prime(54))
