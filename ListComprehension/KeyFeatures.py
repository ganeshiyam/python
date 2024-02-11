"""
List = [1, 2, "a", 3.14]

List Comprehension:

    [expr for val in collection(iterable)]

    [expr for val in collection(iterable) if <test>]

    [expr for val in collection(iterable) if <test1> and <test2>]

    [expr for val1 in collection1(iterable) and val2 in collection2(iterable)]

"""

squares = [i ** 2 for i in range(1, 50)]
print(squares)

remainder = [x ** 2 % 5 for x in range(1, 101)]
print(remainder)

remainder1 = [x ** 2 % 11 for x in range(1, 101)]
print(remainder1)

"""
Quadratic Reciprocity

p_remainders = [x ** 2 % p for x in range(0, p)]

len(p_remainders) = (p + 1) / 2

"""

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind",
          "Citizen Kane", "It's a wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbuster",
          "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the lost Ark",
          "Groundhog Day", "Close Encounters of the Third Kind"]

gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

movies1 = [("Star Wars", 1976), ("Gandhi", 1945), ("Casablanca", 1930), ("Shawshank Redemption", 1960),
           ("Toy Story", 1990), ("Gone with the Wind", 1981), ("Citizen Kane", 1941), ("It's a wonderful Life", 1971),
           ("The Wizard of Oz", 2000), ("Gattaca", 2001), ("Rear Window", 1997), ("Ghostbuster", 1999),
           ("To Kill A Mockingbird", 1983), ("Good Will Hunting", 2003), ("2001: A Space Odyssey", 2001),
           ("Raiders of the lost Ark", 2010), ("Groundhog Day", 1975), ("Close Encounters of the Third Kind", 1965)]

pre2Kmovies = [title for (title, year) in movies1 if year < 2000]
print(pre2Kmovies)

v = [2, -3, 1]

v4 = [4 * x for x in v]
print(v4)

"""
Cartesian Product

If A & B are sets, then the Cartesian product is the set of pairs (a, b) where 'a' is in A and 'b' is in B.

A x B = { (a, b) | a E A, b E B } 

"""

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)

"""
Functions inside List Comprehension
"""
nums = [1, 2, 3, 4, 5, 6]


def timesFive(num):
    return num * 5


result = []
for i in nums:
    i = timesFive(i)
    print(i)
    result.append(i)

new_nums = [timesFive(i) for i in nums]

print(result, new_nums)

"""
List of Dictionaries 

"""

dicts = [{"name": "John"}, {"name": "Matt"}]
# Grab names from dict

result = []
for i in dicts:
    result.append(i['name'])

print(result)

result1 = [i['name'] for i in dicts]

print(result1)
