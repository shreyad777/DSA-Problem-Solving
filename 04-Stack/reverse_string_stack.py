def reverse_string(text):

    stack = []

    # Push every character
    for char in text:
        stack.append(char)

    # Pop characters to reverse the string
    reversed_text = ""

    while stack:
        reversed_text += stack.pop()

    return reversed_text


text = "hello"

result = reverse_string(text)

print("Original:", text)
print("Reversed:", result)