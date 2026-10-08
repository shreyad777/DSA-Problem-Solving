class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x):
        self.input_stack.append(x)

    def pop(self):

        self.move_elements()

        return self.output_stack.pop()

    def peek(self):

        self.move_elements()

        return self.output_stack[-1]

    def empty(self):

        return len(self.input_stack) == 0 and len(self.output_stack) == 0

    def move_elements(self):

        if not self.output_stack:

            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )


queue = MyQueue()

while True:

    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Empty")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        value = int(input("Enter value: "))
        queue.push(value)

        print("Inserted:", value)

    elif choice == "2":

        if queue.empty():
            print("Queue is empty")
        else:
            print("Removed:", queue.pop())

    elif choice == "3":

        if queue.empty():
            print("Queue is empty")
        else:
            print("Front:", queue.peek())

    elif choice == "4":

        print("Queue empty:", queue.empty())

    elif choice == "5":

        print("Program ended.")
        break

    else:
        print("Invalid choice.")
        