def remove_duplicates(text):

    seen = set()
    result = ""

    for char in text:

        if char not in seen:
            seen.add(char)
            result += char

    return result


text = "programming"

result = remove_duplicates(text)

print("Original string:", text)
print("After removing duplicates:", result)

