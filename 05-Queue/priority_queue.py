import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data, priority):
        heapq.heappush(self.queue, (priority, data))

    def dequeue(self):

        if not self.queue:
            return None

        priority, data = heapq.heappop(self.queue)

        return data

    def front(self):

        if not self.queue:
            return None

        priority, data = self.queue[0]

        return data

    def is_empty(self):
        return len(self.queue) == 0


# Create priority queue
pq = PriorityQueue()


# Add elements
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)


# Display highest priority
print("Highest priority:", pq.front())


# Remove elements
print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())


# Check empty
print("Is empty:", pq.is_empty())