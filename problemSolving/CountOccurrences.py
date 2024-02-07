def count_occurrences(num, target):
    count = 0
    for i in num:
        if i == target:
            count += 1
    return count

def count_occur(num1, tgt):
    return num1.count(tgt)
print(count_occurrences([1, 2, 3, 4, 2, 2, 5, 6, 3, 1], 2))
print(count_occur([1, 2, 3, 4, 2, 2, 5, 6, 3, 1], 1))