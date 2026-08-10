class Stack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, data):

        self.q2.append(data)

        while self.q1:
            self.q2.append(self.q1.pop(0))

        self.q1, self.q2 = self.q2, self.q1

    def pop(self):

        if not self.q1:
            return None

        return self.q1.pop(0)

    def top(self):

        if not self.q1:
            return None

        return self.q1[0]

    def is_empty(self):
        return len(self.q1) == 0


# Create stack
stack = Stack()


# Push elements
stack.push(10)
stack.push(20)
stack.push(30)


print("Top:", stack.top())

print("Removed:", stack.pop())

print("Top after pop:", stack.top())

print("Is empty:", stack.is_empty())
