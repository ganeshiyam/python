# Calculate Sum of Digits
# Write a function called sum_of_digits that takes a positive integer as an argument and returns the sum of its digits.

def sum_of_digits(n: int):
    sn = str(n)
    sum = 0
    for i in sn:
        sum += int(i)
    return sum
    # return sum(int(digit) for digit in str(n))

print(sum_of_digits(12780))