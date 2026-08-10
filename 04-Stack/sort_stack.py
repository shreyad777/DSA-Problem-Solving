def sort_stack(stack):

    temp_stack = []

    while stack:

        current = stack.pop()

        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())

        temp_stack.append(current)

    return temp_stack

stack = [30, 10, 50, 20, 40]

sorted_stack = sort_stack(stack)

print("Original stack:", stack)
print("Sorted stack:", sorted_stack)