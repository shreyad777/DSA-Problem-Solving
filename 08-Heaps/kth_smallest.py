import heapq


def kth_smallest(arr, k):

    max_heap = []

    for num in arr:

        heapq.heappush(max_heap, -num)

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return -max_heap[0]


# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3

result = kth_smallest(arr, k)

print("Kth smallest element:", result)
