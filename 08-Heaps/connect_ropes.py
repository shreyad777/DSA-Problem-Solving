import heapq
def minimum_cost(ropes):
    if len(ropes) <= 1:
        return 0
    heapq.heapify(ropes)
    total_cost = 0
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost += cost
        heapq.heappush(ropes, cost)
    return total_cost
ropes = [4, 3, 2, 6]
result = minimum_cost(ropes)
print("Minimum cost:", result)