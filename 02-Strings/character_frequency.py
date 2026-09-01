def character_frequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
text = "hello"
result = character_frequency(text)
print("String:", text)
print("Character frequency:", result)