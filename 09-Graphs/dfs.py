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

    # DFS traversal
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

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

# Perform DFS
result = g.dfs(0)

print("DFS Traversal:", result)