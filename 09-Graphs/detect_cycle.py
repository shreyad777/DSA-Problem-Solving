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

    # Detect cycle using DFS
    def has_cycle(self):

        visited = set()

        def dfs(vertex, parent):

            visited.add(vertex)

            for neighbor in self.graph[vertex]:

                # If neighbor is not visited,
                # continue DFS
                if neighbor not in visited:

                    if dfs(neighbor, vertex):
                        return True

                # If already visited and not parent,
                # cycle exists
                elif neighbor != parent:

                    return True

            return False

        # Handle disconnected graphs
        for vertex in self.graph:

            if vertex not in visited:

                if dfs(vertex, -1):
                    return True

        return False


# Example graph with a cycle

g = Graph()

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

print("Graph has cycle:", g.has_cycle())