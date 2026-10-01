class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.min_stack[-1]
operations = input(
    "Enter operations separated by spaces: "
).split()
values = input(
    "Enter values separated by spaces: "
).split()
stack = MinStack()
value_index = 0

for operation in operations:

    if operation == "push":
        value = int(values[value_index])
        value_index += 1

        stack.push(value)
        print("Pushed:", value)

    elif operation == "pop":
        stack.pop()
        print("Popped")

    elif operation == "top":
        print("Top:", stack.top())

    elif operation == "min":
        print("Minimum:", stack.getMin())