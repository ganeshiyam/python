def is_balanced_parentheses(s):
    stack = []
    parentheses_mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in parentheses_mapping.values():
            stack.append(char)
        elif char in parentheses_mapping.keys():
            if not stack or stack.pop() != parentheses_mapping[char]:
                return False
        else:
            return False
    return not stack


print(is_balanced_parentheses("()"))
print(is_balanced_parentheses("()[]{}"))
print(is_balanced_parentheses("(]"))
print(is_balanced_parentheses("([)]"))
print(is_balanced_parentheses("{[]}"))
