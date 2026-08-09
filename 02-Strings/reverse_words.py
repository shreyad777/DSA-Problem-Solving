def reverse_words(text):

    words = text.split()

    return " ".join(words[::-1])


text = "I love Python"

result = reverse_words(text)

print("Original sentence:", text)
print("Reversed words:", result)