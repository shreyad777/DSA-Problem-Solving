import heapq
def top_k_frequent(arr, k):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    min_heap = []
    for num, count in frequency.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    result = []
    while min_heap:
        count, num = heapq.heappop(min_heap)
        result.append(num)
    return result
arr = [1, 1, 1, 2, 2, 3]
k = 2
result = top_k_frequent(arr, k)
print("Top K frequent elements:", result)