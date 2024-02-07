def find_missing_number(nums: int):
    '''
    :param nums: int
    :return: int
    '''
    n = len(nums)
    total_sum = (n * (n + 1)) // 2 # Sum of first n+1 natural numbers
    return total_sum - sum(nums)

print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 8, 9]))