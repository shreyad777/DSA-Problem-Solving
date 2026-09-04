class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, data):
        self.stack1.append(data)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()
    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2[-1]
    def is_empty(self):
        return not self.stack1 and not self.stack2
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Front:", queue.front())
print("Removed:", queue.dequeue())
print("Removed:", queue.dequeue())
print("Front:", queue.front())
print("Is empty:", queue.is_empty())