class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):

        if not self.queue:
            return None

        return self.queue.pop(0)

    def front(self):

        if not self.queue:
            return None

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


# Create Queue
queue = Queue()


# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)


# Display front
print("Front:", queue.front())


# Dequeue
print("Removed:", queue.dequeue())


# Display front after dequeue
print("Front after dequeue:", queue.front())


# Check if empty
print("Is empty:", queue.is_empty())