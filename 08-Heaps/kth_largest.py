import heapq


def kth_largest(arr, k):

    min_heap = []

    for num in arr:

        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]


# Example
arr = [3, 2, 1, 5, 6, 4]
k = 2

result = kth_largest(arr, k)

print("Kth largest element:", result)