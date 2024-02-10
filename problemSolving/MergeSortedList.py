"""
merge_sorted_lists that takes two sorted lists of integers as input and returns a single sorted list containing all the
elements from both input lists
"""


def merge_sorted_lists(list1, list2):
    # Your code here
    list3 = list1 + list2
    sort_list = sorted(list3)
    return sort_list


def merge_sorted_lists1(list1, list2):
    merged_list = []

    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

        # Append any remaining elements from both lists (if any)
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list


if __name__ == "__main__":
    print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([1, 4, 6], [2, 3, 5]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([], [1, 2, 3]))  # [1, 2, 3]
    print(merge_sorted_lists([1, 2, 3], []))  # [1, 2, 3]
    print(merge_sorted_lists([], []))  # []
    print(merge_sorted_lists1([11, 13, 15], [12, 14, 16]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists1([11, 21, 31], [41, 51, 61]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists1([11, 14, 16], [12, 13, 15]))  # [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists1([], [11, 12, 13]))  # [1, 2, 3]
    print(merge_sorted_lists1([11, 21, 31], []))  # [1, 2, 3]
    print(merge_sorted_lists1([], []))  # []
