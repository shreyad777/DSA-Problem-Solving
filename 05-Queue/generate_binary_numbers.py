from collections import deque
def generate_binary(n):
    if n <= 0:
        return []
    queue = deque()
    queue.append("1")
    result = []
    for _ in range(n):
        current = queue.popleft()
        result.append(current)
        queue.append(current + "0")
        queue.append(current + "1")
    return result
n = 5
result = generate_binary(n)
print("N:", n)
print("Binary numbers:")
for number in result:
    print(number)