import heapq

def minimum_cost(ropes):

    if len(ropes) <= 1:
        return 0

    # Convert list into a min heap
    heapq.heapify(ropes)

    total_cost = 0

    while len(ropes) > 1:

        # Remove two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        # Cost of connecting them
        cost = first + second

        total_cost += cost

        # Add the combined rope back
        heapq.heappush(ropes, cost)

    return total_cost


# Example
ropes = [4, 3, 2, 6]

result = minimum_cost(ropes)

print("Minimum cost:", result)