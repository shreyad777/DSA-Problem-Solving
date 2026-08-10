def remove_duplicates(string):

    stack = []

    for char in string:

        if not stack:
            stack.append(char)

        elif stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    return ''.join(stack)

string = "abbaca"

result = remove_duplicates(string)

print("Original:", string)
print("After removing duplicates:", result)
