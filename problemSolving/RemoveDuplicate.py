def remove_duplicates(input_list):
    res = []
    [res.append(i) for i in input_list if i not in res]
    return res

print(remove_duplicates(['apple', 'banana', 'apple', 'cherry']))
print(remove_duplicates([1, 2, 3]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))