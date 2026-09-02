def find_longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
text = "I love programming"
result = find_longest_word(text)
print("Sentence:", text)
print("Longest word:", result)