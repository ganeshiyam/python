'''
List of opererations,
- sorted on a list with element as non tuple
- sorted on a list with tuples as tuple (key as 2nd entry)
- list comprehension
'''


sample = [(9, 4, 3), (3, 5, 7), (1, 0, 1)]
print(sorted(sample))

print(sorted(sample, key=lambda x: x[1]))
