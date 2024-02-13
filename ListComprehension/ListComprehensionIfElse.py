"""
If else in List comprehension
If else after for is filter conditional
If else before for is just a conditional
"""

list1 = [1, 2, 3]
result = [i for i in list1]
result1 = [i for i in list1 if i > 1]
result2 = [i * 5 for i in list1 if i > 2]  # Filter conditional
result3 = [i * 5 for i in list1]
result4 = [i * 5 if i == 3 else i for i in list1]  # Just conditional
result5 = [i * 5 if i == 3 else i for i in list1 if i == 1]     # Conditional & Filter
result6 = [i * 5 if i == 3 else i for i in list1 if i > 1]
result7 = [i * 5 if i == 3 else i for i in list1 if i > 10]


if __name__ == "__main__":
    print(result, '\n', result1, '\n', result2, '\n', result3, '\n', result4, '\n', result5, '\n', result6, '\n',
          result7)
