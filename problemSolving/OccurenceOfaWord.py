def count_word_occurrences(text, word):
    text_list = text.lower().split()
    count = 0
    for i in text_list:
        if i == word:
            count += 1
    return count

def count_word_occur(text1, word):
    text1 = text1.lower()
    word = word.lower()
    return text1.count(word) if text1 else 0

print(count_word_occurrences("The quick brown fox jumps over the lazy dog.", "the"))
print(count_word_occurrences("This is a test sentence. This sentence is a test.", "sentence"))
print(count_word_occurrences("Python is a versatile programming language.", "Python"))
print(count_word_occurrences("No matches here.", "word"))

print(count_word_occur("The quick brown fox jumps over the lazy dog.", "the"))
print(count_word_occur("This is a test sentence. This sentence is a test.", "sentence"))
print(count_word_occur("Python is a versatile programming language.", "Python"))
print(count_word_occur("No matches here.", "word"))