from collections import deque


def josephus(n, k):

    if n <= 0 or k <= 0:
        return None

    queue = deque(range(1, n + 1))

    while len(queue) > 1:

        for _ in range(k - 1):
            queue.append(queue.popleft())

        queue.popleft()

    return queue[0]


# Test
n = 7
k = 3

result = josephus(n, k)

print("Number of people:", n)
print("Step:", k)
print("Last remaining person:", result)
