class CustomStack:

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1

        return self.stack.pop()

    def increment(self, k, val):
        limit = min(k, len(self.stack))

        for i in range(limit):
            self.stack[i] += val


max_size = int(input("Enter maximum stack size: "))

stack = CustomStack(max_size)

operations = input(
    "Enter operations separated by spaces: "
).split()

values = input(
    "Enter values for push/increment operations: "
).split()

value_index = 0

for operation in operations:

    if operation == "push":
        value = int(values[value_index])
        value_index += 1

        stack.push(value)
        print("Push:", value)

    elif operation == "pop":
        print("Pop:", stack.pop())

    elif operation == "increment":
        k = int(values[value_index])
        val = int(values[value_index + 1])
        value_index += 2

        stack.increment(k, val)

        print(
            "Increment:",
            k,
            "elements by",
            val
        )
        