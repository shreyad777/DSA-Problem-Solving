class MinHeap:

    def __init__(self):
        self.heap = []

    # Insert an element
    def insert(self, value):

        self.heap.append(value)

        index = len(self.heap) - 1

        # Heapify up
        while index > 0:

            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:

                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]

                index = parent

            else:
                break

    # Get minimum element
    def get_min(self):

        if not self.heap:
            return None

        return self.heap[0]

    # Remove minimum element
    def extract_min(self):

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]

        self.heap[0] = self.heap.pop()

        index = 0

        # Heapify down
        while True:

            left = 2 * index + 1
            right = 2 * index + 2

            smallest = index

            if left < len(self.heap) and \
                    self.heap[left] < self.heap[smallest]:

                smallest = left

            if right < len(self.heap) and \
                    self.heap[right] < self.heap[smallest]:

                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = \
                self.heap[smallest], self.heap[index]

            index = smallest

        return minimum


# Create heap
min_heap = MinHeap()


# Insert elements
min_heap.insert(20)
min_heap.insert(10)
min_heap.insert(30)
min_heap.insert(5)
min_heap.insert(40)


print("Heap:", min_heap.heap)

print("Minimum:", min_heap.get_min())

print("Extracted:", min_heap.extract_min())

print("Heap after extraction:", min_heap.heap)

print("New minimum:", min_heap.get_min())