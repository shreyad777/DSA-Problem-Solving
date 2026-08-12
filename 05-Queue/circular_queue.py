class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, data):

        if self.count == self.size:
            print("Queue is full")
            return

        self.queue[self.rear] = data

        self.rear = (self.rear + 1) % self.size

        self.count += 1

    def dequeue(self):

        if self.count == 0:
            print("Queue is empty")
            return None

        data = self.queue[self.front]

        self.queue[self.front] = None

        self.front = (self.front + 1) % self.size

        self.count -= 1

        return data

    def display(self):

        if self.count == 0:
            print("Queue is empty")
            return

        index = self.front

        for _ in range(self.count):

            print(self.queue[index], end=" ")

            index = (index + 1) % self.size

        print()

cq = CircularQueue(5)


# Add elements
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)


print("Queue:")
cq.display()


# Remove elements
print("Removed:", cq.dequeue())
print("Removed:", cq.dequeue())


# Add new elements
cq.enqueue(60)
cq.enqueue(70)


print("Queue after circular insertion:")
cq.display()