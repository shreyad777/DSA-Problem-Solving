import heapq

class PriorityQueue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item, priority):

        heapq.heappush(
            self.queue,
            (priority, item)
        )

    # Remove highest-priority element
    def dequeue(self):

        if not self.queue:
            return None

        priority, item = heapq.heappop(self.queue)

        return item

    # View highest-priority element
    def peek(self):

        if not self.queue:
            return None

        priority, item = self.queue[0]

        return item

    # Check whether queue is empty
    def is_empty(self):

        return len(self.queue) == 0


# Create Priority Queue
pq = PriorityQueue()

# Add elements
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print("Highest priority:", pq.peek())

print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())

print("Is empty:", pq.is_empty())