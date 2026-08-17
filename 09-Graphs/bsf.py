from collections import deque


class Graph:

    def __init__(self):
        self.graph = {}

    # Add vertex
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add undirected edge
    def add_edge(self, vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # BFS traversal
    def bfs(self, start):

        visited = set()

        queue = deque()

        # Start with the starting vertex
        queue.append(start)
        visited.add(start)

        result = []

        while queue:

            vertex = queue.popleft()

            result.append(vertex)

            # Visit neighbors
            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


# Create graph
g = Graph()

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

# Perform BFS
result = g.bfs(0)

print("BFS Traversal:", result)