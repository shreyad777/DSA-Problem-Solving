from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q = deque()

    # Push element into stack
    def push(self, x):
        self.q.append(x)

        # Move all previous elements behind the new element
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    # Remove top element
    def pop(self):
        if not self.q:
            return "Stack is empty"
        return self.q.popleft()

    # Return top element
    def peek(self):
        if not self.q:
            return "Stack is empty"
        return self.q[0]

    # Check if stack is empty
    def is_empty(self):
        return len(self.q) == 0


# Example
stack = StackUsingQueue()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Top element:", stack.peek())