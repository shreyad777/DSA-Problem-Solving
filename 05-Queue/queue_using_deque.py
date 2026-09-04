from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()
    def front(self):
        if not self.queue:
            return None
        return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front:", queue.front())
print("Removed:", queue.dequeue())
print("Front after dequeue:", queue.front())
print("Is empty:", queue.is_empty())