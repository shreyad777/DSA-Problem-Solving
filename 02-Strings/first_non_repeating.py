def first_non_repeating(text):

    frequency = {}

    for char in text:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in text:

        if frequency[char] == 1:
            return char

    return None


text = "swiss"

result = first_non_repeating(text)

print("String:", text)
print("First non-repeating character:", result)