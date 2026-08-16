import heapq

def top_k_frequent(arr, k):

    # Step 1: Count frequency
    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    # Step 2: Create min heap
    min_heap = []

    for num, count in frequency.items():

        heapq.heappush(min_heap, (count, num))

        # Keep only k elements
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 3: Extract elements
    result = []

    while min_heap:
        count, num = heapq.heappop(min_heap)
        result.append(num)

    return result


# Example
arr = [1, 1, 1, 2, 2, 3]
k = 2

result = top_k_frequent(arr, k)

print("Top K frequent elements:", result)