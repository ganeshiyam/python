# Introduction to List Comprehension

# Basic approach for the Squares of numbers
def squares(nums):
    square = []

    for i in nums:
        square.append(i ** 2)

    return square


# List Comprehension

def squares1(nums):
    square1 = [i ** 2 for i in nums]
    square2 = [i ** 2 for i in range(1, 101)]
    return square1, square2


def multiples(nums):
    multiple = [i * 2 for i in nums]
    return multiple


if __name__ == "__main__":
    print(squares([1, 2, 3]))
    print(squares1([1, 2, 3]))
    print(multiples([1, 2, 3, 4, 5, 6]))
