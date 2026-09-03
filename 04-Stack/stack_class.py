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
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack:")
stack.display()
print("Top element:", stack.peek())
removed = stack.pop()
print("Removed:", removed)
print("Stack after pop:")
stack.display()
print("Is stack empty?", stack.is_empty())