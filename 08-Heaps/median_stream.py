import heapq

class MedianFinder:

    def __init__(self):

        # Max heap for smaller half
        self.max_heap = []

        # Min heap for larger half
        self.min_heap = []

    def add_num(self, num):

        # Add to max heap first
        heapq.heappush(self.max_heap, -num)

        # Make sure every element in max_heap
        # is <= every element in min_heap
        if self.max_heap and self.min_heap:

            if -self.max_heap[0] > self.min_heap[0]:

                max_value = -heapq.heappop(self.max_heap)
                min_value = heapq.heappop(self.min_heap)

                heapq.heappush(self.max_heap, -min_value)
                heapq.heappush(self.min_heap, max_value)

        # Balance the sizes

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


# Example
finder = MedianFinder()

numbers = [5, 10, 15, 20, 25]

for num in numbers:

    finder.add_num(num)

    print(
        "Added:", num,
        "Median:", finder.find_median()
    )