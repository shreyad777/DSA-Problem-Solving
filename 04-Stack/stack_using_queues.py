from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self):
        if not self.q:
            return "Stack is empty"
        return self.q.popleft()
    def peek(self):
        if not self.q:
            return "Stack is empty"
        return self.q[0]
    def is_empty(self):
        return len(self.q) == 0
stack = StackUsingQueue()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Top element:", stack.peek())