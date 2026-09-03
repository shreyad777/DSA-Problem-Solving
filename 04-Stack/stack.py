stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)
removed = stack.pop()
print("Removed:", removed)
print("Stack after pop:", stack)
if stack:
    print("Top element:", stack[-1])
else:
    print("Stack is empty")
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")