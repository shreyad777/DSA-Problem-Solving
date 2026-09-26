class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0
    def push(self, val):
        self.freq[val] = self.freq.get(val, 0) + 1
        frequency = self.freq[val]
        if frequency not in self.group:
            self.group[frequency] = []
        self.group[frequency].append(val)
        self.max_freq = max(
            self.max_freq,
            frequency
        )
    def pop(self):
        # Get most recent value
        val = self.group[self.max_freq].pop()

        # Decrease its frequency
        self.freq[val] -= 1

        # If this frequency stack becomes empty
        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val


freq_stack = FreqStack()

operations = input(
    "Enter operations separated by spaces: "
).split()

result = []

for operation in operations:

    if operation.startswith("push"):
        value = int(
            operation.split("(")[1].split(")")[0]
        )

        freq_stack.push(value)

    elif operation == "pop":
        result.append(freq_stack.pop())


print("Pop Results:", result)