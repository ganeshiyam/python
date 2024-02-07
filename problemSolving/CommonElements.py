def find_common_elements(lst1, lst2: int):
    common_lst = [value for value in lst1 if value in lst2]
    return common_lst


print(find_common_elements([4, 9, 1, 17, 11, 26, 28, 54, 69], [9, 9, 74, 21, 45, 11, 63, 28, 26]))