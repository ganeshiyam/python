nums = [1, 2, 3, 4]
result = [i for i in nums]
result1 = [i for i in nums if i > 2]
result2 = [i for i in nums if i > 1 if i != 3]  # Multiple If
result3 = [i for i in nums if i > 1 and i != 3]  # Condition with if AND

fruits = ['Apples', 'Peaches', 'Pears', 'Bananas']
result4 = [(i, f) for i in nums if i > 1 for f in fruits]   # Multiple For Loop

for i in nums:
    if i > 1:
        for f in fruits:
            print(i, f)

result5 = [(i, f) for i in nums if i > 1 if i != 3 for f in fruits if f != 'Pears']   # Multiple For & If Loop

for i in nums:
    if i > 1:
        if i != 3:
            for f in fruits:
                if f != 'Pears':
                    print(i, f)
                

result6 = [(i, f) for i in nums if i > 1 if i != 3 for f in fruits if f != 'Pears' and f != 'Apples']   # Multiple For & If Loop

for i in nums:
    if i > 1:
        if i != 3:
            for f in fruits:
                if f != 'Pears' and f != 'Apples':
                    print(i, f)

if __name__ == "__main__":
    print(result, '\n', result1, '\n', result2, '\n', result3, '\n', result4, '\n', result5, '\n', result6)
