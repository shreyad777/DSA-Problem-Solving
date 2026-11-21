class MyCircularDeque:
    def __init__(self, k):
        self.size = k
        self.deque = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
    def insertFront(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.size
        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value):

        if self.isFull():
            return False

        if self.isEmpty():
            self.front = 0
            self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.deque[self.rear] = value
        self.count += 1

        return True

    def deleteFront(self):

        if self.isEmpty():
            return False

        if self.count == 1:
            self.front = 0
            self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

        self.count -= 1
        return True

    def deleteLast(self):

        if self.isEmpty():
            return False

        if self.count == 1:
            self.front = 0
            self.rear = -1

        else:
            self.rear = (self.rear - 1) % self.size

        self.count -= 1
        return True

    def getFront(self):

        if self.isEmpty():
            return -1

        return self.deque[self.front]

    def getRear(self):

        if self.isEmpty():
            return -1

        return self.deque[self.rear]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size


capacity = int(input("Enter deque capacity: "))

dq = MyCircularDeque(capacity)

while True:

    print("\n1. Insert Front")
    print("2. Insert Rear")
    print("3. Delete Front")
    print("4. Delete Rear")
    print("5. Get Front")
    print("6. Get Rear")
    print("7. Check Empty")
    print("8. Check Full")
    print("9. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        value = int(input("Enter value: "))
        print("Inserted:", dq.insertFront(value))

    elif choice == "2":
        value = int(input("Enter value: "))
        print("Inserted:", dq.insertLast(value))

    elif choice == "3":
        print("Deleted:", dq.deleteFront())

    elif choice == "4":
        print("Deleted:", dq.deleteLast())

    elif choice == "5":
        print("Front:", dq.getFront())

    elif choice == "6":
        print("Rear:", dq.getRear())

    elif choice == "7":
        print("Is Empty:", dq.isEmpty())

    elif choice == "8":
        print("Is Full:", dq.isFull())

    elif choice == "9":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")