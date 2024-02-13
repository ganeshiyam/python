"""
List Comprehension vs map() function

List Comprehension - [expr for x in list(iterable)]

map() - map(function, List(iterable)
"""
from timeit import timeit

a = [1, 2, 3, 4]
result = [x * 2 for x in a]
result1 = list(map(lambda x: x * 2, a))
result21 = [str(x) for x in [1, 2, 3, 4]]
result22 = list(map(str, [1, 2, 3, 4]))
result31 = [str(x) for x in [1, 2, 3, 4] if x > 1]
result32 = list(map(lambda x: str(x), filter(lambda x: x > 1, a)))


def timesTwo(num):
    return num * 2


result11 = [timesTwo(x) for x in a]  # List Comprehension
result12 = list(map(timesTwo, a))  # map function without lambda

timeit11 = timeit("list(map(timesTwo, a))")
timeit1 = timeit("list(map(lambda x: x * 2, a))")


if __name__ == "__main__":
    print(result, '\n', result1)
    print(result11, result12)
    print(result21, result22)
    print(result31, result32)


