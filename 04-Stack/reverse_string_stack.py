def reverse_string(text):
    stack = []
    for char in text:
        stack.append(char)
    reversed_text = ""
    while stack:
        reversed_text += stack.pop()
    return reversed_text
text = "hello"
result = reverse_string(text)
print("Original:", text)
print("Reversed:", result)