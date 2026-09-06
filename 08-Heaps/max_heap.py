class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break
    def get_max(self):
        if not self.heap:
            return None
        return self.heap[0]
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < len(self.heap) and \
                    self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and \
                    self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = \
                self.heap[largest], self.heap[index]
            index = largest
        return maximum
max_heap = MaxHeap()
max_heap.insert(20)
max_heap.insert(40)
max_heap.insert(10)
max_heap.insert(50)
max_heap.insert(30)
print("Heap:", max_heap.heap)
print("Maximum:", max_heap.get_max())
print("Extracted:", max_heap.extract_max())
print("Heap after extraction:", max_heap.heap)
print("New maximum:", max_heap.get_max())