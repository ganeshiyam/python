# Basic String Comprehension
def upper_case(strings):
    results = []
    for i in strings:
        i = i.upper()
        results.append(i)
    return results


# String List Comprehension
def upper_case1(strings):
    upper_case_strings = [i.upper() for i in strings]   # List Comprehension
    return upper_case_strings


if __name__ == "__main__":
    print(upper_case(["intro", "to", "list", "comps"]))
    print(upper_case1(["fun", "to", "learn", "list", "comps"]))
