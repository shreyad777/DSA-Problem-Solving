from collections import deque


def is_bipartite(graph):

    n = len(graph)

    # -1 means not colored
    color = [-1] * n

    for start in range(n):

        # Skip already colored component
        if color[start] != -1:
            continue

        # Start with color 0
        color[start] = 0

        queue = deque([start])

        while queue:

            vertex = queue.popleft()

            for neighbor in graph[vertex]:

                # If neighbor is not colored
                if color[neighbor] == -1:

                    color[neighbor] = 1 - color[vertex]

                    queue.append(neighbor)

                # Same color on both ends
                elif color[neighbor] == color[vertex]:

                    return False

    return True


# Example

graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]


if is_bipartite(graph):

    print("The graph is bipartite.")

else:

    print("The graph is not bipartite.")