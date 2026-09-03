class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, data):
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)
    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
stack = MinStack()
stack.push(30)
stack.push(10)
stack.push(50)
stack.push(20)
print("Minimum:", stack.get_min())
stack.pop()
print("Minimum after pop:", stack.get_min())