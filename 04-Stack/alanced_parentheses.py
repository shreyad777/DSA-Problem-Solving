def is_balanced(expression):

    stack = []

    for char in expression:

        if char == '(':
            stack.append(char)

        elif char == ')':

            if not stack:
                return False

            stack.pop()

    return len(stack) == 0


# Test expression
expression = "(a + b)"

if is_balanced(expression):
    print("Balanced")
else:
    print("Not Balanced")
