# Check Palindrome
# Write a function called is_palindrome that takes a string as an argument and returns True if it('s a palindrome, and False otherwise. '
# 'A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backward as forwards, such as madam or racecar.)

def is_palindrome(word: str):
    w = word.lower()
    return w[::-1] == w

print(is_palindrome("racecar"))