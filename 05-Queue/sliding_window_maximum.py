from collections import deque


def sliding_window_maximum(array, k):

    if not array or k <= 0:
        return []

    if k > len(array):
        return []

    dq = deque()
    result = []

    for i in range(len(array)):

        # Remove indices outside the current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements
        while dq and array[dq[-1]] <= array[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Add maximum of current window
        if i >= k - 1:
            result.append(array[dq[0]])

    return result


# Test
array = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

result = sliding_window_maximum(array, k)

print("Array:", array)
print("Window size:", k)
print("Maximum values:", result)
