class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):

        if not self.items:
            return None

        return self.items.pop()

    def peek(self):

        if not self.items:
            return None

        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

# Create stack
stack = Stack()


# Push elements
stack.push(10)
stack.push(20)
stack.push(30)


print("Stack:")
stack.display()


# Peek
print("Top element:", stack.peek())


# Pop
removed = stack.pop()

print("Removed:", removed)


# Display after pop
print("Stack after pop:")
stack.display()


# Check if empty
print("Is stack empty?", stack.is_empty())