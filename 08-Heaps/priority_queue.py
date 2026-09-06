import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item, priority):

        heapq.heappush(
            self.queue,
            (priority, item)
        )
    def dequeue(self):
        if not self.queue:
            return None
        priority, item = heapq.heappop(self.queue)
        return item
    def peek(self):
        if not self.queue:
            return None
        priority, item = self.queue[0]
        return item
    def is_empty(self):
        return len(self.queue) == 0
pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
print("Highest priority:", pq.peek())
print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())
print("Removed:", pq.dequeue())
print("Is empty:", pq.is_empty())