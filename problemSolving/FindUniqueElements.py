# Find Unique Elements
# Find the unique elements of a list: In: [1,3,4,5,6,7] Out: 6 In: [1,1,3,4,5,5,6,7]
# Out: 6 (1 and 5 are duplicated and should be counted once)

def find_unique_element(lst):
    '''
    :param lst: list
    :return: int
    '''
    return len(set(lst))

print(find_unique_element([1,3,4,5,6,7]))
print(find_unique_element([1,1,3,4,5,5,6,7]))