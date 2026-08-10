stack = []


# Push elements
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)


# Pop the top element
removed = stack.pop()

print("Removed:", removed)
print("Stack after pop:", stack)


# Peek at the top element
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")


# Check whether stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")