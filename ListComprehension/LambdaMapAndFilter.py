"""
[a if condition1 else b for i in list1 if condition2]
EX: [i * 5 if i == 3 else i for i in list1 if i > 10]

The two if's with condition1 and condition2 doing two different things.

The part (a if condition1 else b) is from a lambda expression:
lambda x: a if condition1 else b

while the other condition2 is another lambda:
lambda x: condition2

Whole list comprehension can be regard as combination of map and filter:
map(lambda x: a if condition2 else b, filter(lambda x: condition2, list1))
"""

list1 = [1, 2, 3]
result = [i * 5 if i == 3 else i for i in list1]
result1 = list(map(lambda i: i * 5, list1))  # Map (Lambda)
result2 = list(map(lambda i: i * 5 if i == 3 else i, list1))

result3 = [i * 5 if i == 3 else i for i in list1 if i > 1]
result4 = list(map(lambda i: i * 5 if i == 3 else i, filter(lambda i: i > 1, list1)))

if __name__ == "__main__":
    print(result, '\n', result1, '\n', result2, '\n', result3, '\n', result4)
