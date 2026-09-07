from collections import deque
def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbor in graph[vertex]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[vertex]
                    queue.append(neighbor)
                elif color[neighbor] == color[vertex]:
                    return False
    return True
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