"""
Longest_consecutive_subsequence that takes a list of integers as input and returns the length of the longest consecutive
 subsequence of integers in the list. A consecutive subsequence is a sequence of integers where each integer appears
 exactly once, and they are in consecutive order
"""

def longest_consecutive_subsequence(nums):
    num_set = set(nums)
    consecutive_subseq = []
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                consecutive_subseq.append(current_num)
            max_length = max(max_length, current_length)

    return max_length, consecutive_subseq


if __name__ == "__main__":
    print(longest_consecutive_subsequence([100, 4, 200, 1, 3, 2]))  # The longest consecutive subsequence is [1, 2,
    # 3, 4].
    print(longest_consecutive_subsequence([5, 2, 99, 3, 4, 1]))  # The longest consecutive subsequence is [1, 2, 3,
    # 4, 5].
    print(longest_consecutive_subsequence([1, 2, 3, 4, 5]))  # The list is already a consecutive subsequence.
    print(longest_consecutive_subsequence([5, 4, 3, 2, 1]))  # The list is already a consecutive subsequence (reverse
    # order).
    print(longest_consecutive_subsequence([]))  # The list is empty.
