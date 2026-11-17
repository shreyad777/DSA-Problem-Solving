class MyCircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
    def enQueue(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True
    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True
    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        return self.count == self.size
capacity = int(input("Enter queue capacity: "))
q = MyCircularQueue(capacity)
while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Rear")
    print("5. Check Empty")
    print("6. Check Full")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = int(input("Enter value: "))
        print("Inserted:", q.enQueue(value))

    elif choice == "2":
        print("Deleted:", q.deQueue())

    elif choice == "3":
        print("Front:", q.Front())

    elif choice == "4":
        print("Rear:", q.Rear())

    elif choice == "5":
        print("Is Empty:", q.isEmpty())

    elif choice == "6":
        print("Is Full:", q.isFull())

    elif choice == "7":
        break

    else:
        print("Invalid choice.")
