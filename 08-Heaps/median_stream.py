import heapq
class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
    def add_num(self, num):
        heapq.heappush(self.max_heap, -num)
        if self.max_heap and self.min_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                max_value = -heapq.heappop(self.max_heap)
                min_value = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_value)
                heapq.heappush(self.min_heap, max_value)
        if len(self.max_heap) > len(self.min_heap) + 1:
            value = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, value)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            value = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -value)
    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
finder = MedianFinder()
numbers = [5, 10, 15, 20, 25]
for num in numbers:
    finder.add_num(num)
    print(
        "Added:", num,
        "Median:", finder.find_median()
    )