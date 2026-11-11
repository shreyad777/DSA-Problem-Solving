class MyStack:
    def __init__(self):
        self.queue = []
    def push(self, x):
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
    def pop(self):
        if self.empty():
            return None
        return self.queue.pop(0)
    def top(self):
        if self.empty():
            return None
        return self.queue[0]
    def empty(self):
        return len(self.queue) == 0
stack = MyStack()
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Empty")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        value = int(input("Enter value: "))
        stack.push(value)
        print("Inserted:", value)
    elif choice == "2":
        result = stack.pop()
        print("Popped:", result if result is not None else "Stack is empty")
    elif choice == "3":
        result = stack.top()
        print("Top:", result if result is not None else "Stack is empty")
    elif choice == "4":
        print("Stack empty:", stack.empty())
    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")