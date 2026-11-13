from collections import deque
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self, t):
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
counter = RecentCounter()
n = int(input("Enter number of requests: "))
for i in range(n):
    t = int(input("Enter request time: "))
    print("Recent requests:", counter.ping(t))