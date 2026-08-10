def evaluate_postfix(expression):

    stack = []

    for item in expression.split():

        if item.isdigit():

            stack.append(int(item))

        else:

            b = stack.pop()
            a = stack.pop()

            if item == '+':
                stack.append(a + b)

            elif item == '-':
                stack.append(a - b)

            elif item == '*':
                stack.append(a * b)

            elif item == '/':
                stack.append(a / b)

    return stack[0]

expression = "2 3 +"

result = evaluate_postfix(expression)

print("Expression:", expression)
print("Result:", result)