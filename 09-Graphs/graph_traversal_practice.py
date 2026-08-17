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

    # BFS
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)

        result = []

        while queue:

            vertex = queue.popleft()

            result.append(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    # DFS
    def dfs(self, start):

        visited = set()
        result = []

        def explore(vertex):

            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    explore(neighbor)

        explore(start)

        return result


# Create graph
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(4, 6)


# BFS
print("BFS Traversal:", g.bfs(0))

# DFS
print("DFS Traversal:", g.dfs(0))