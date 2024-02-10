def find_closest_number(numbers, target):
    if not numbers:
        return None

    closest = numbers[0]  # Initialize closest with the first number in the list
    min_diff = abs(target - closest)

    for num in numbers:
        diff = abs(target - num)
        if diff < min_diff:
            closest = num
            min_diff = diff

    return closest


if __name__ == "__main__":
    print(find_closest_number([2, 4, 8, 10], 50))