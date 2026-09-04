from collections import deque
def sliding_window_maximum(array, k):
    if not array or k <= 0:
        return []
    if k > len(array):
        return []
    dq = deque()
    result = []
    for i in range(len(array)):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and array[dq[-1]] <= array[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(array[dq[0]])
    return result
array = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_maximum(array, k)
print("Array:", array)
print("Window size:", k)
print("Maximum values:", result)
