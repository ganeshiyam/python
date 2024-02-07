def calculate_average(num: int):
    avg = 0
    for i in num:
        avg += i / (len(num))
        i += 1
    return avg

def calc_avg(num1: int):
    if len(num1) == 0:
        return 0
    total = sum(num1)
    avg1 = total / len(num1)
    return avg1

print(calculate_average([2, 4, 5, 5]), calc_avg([2, 4, 5, 5]))