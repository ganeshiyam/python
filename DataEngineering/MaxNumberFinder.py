class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums

    def find_max_number(self):
        if not self.nums:
            return None
        return max(self.nums)

    def find_max_number1(self):
        max_num = 0
        for i in sorted(self.nums):
            if i < max_num:
                return None
            else:
                max_num = i
        return f'{max_num}'


if __name__ == "__main__":
    max1 = MaxNumberFinder([9, 1, 2, 3, 4, 5])
    max2 = MaxNumberFinder([19, 11, 21, 33, 14, 65])
    print(max1.find_max_number())
    print(max2.find_max_number1())
