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

    # Find connected components
    def connected_components(self):

        visited = set()
        components = []

        def dfs(vertex, component):

            visited.add(vertex)

            component.append(vertex)

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    dfs(neighbor, component)

        # Check every vertex
        for vertex in self.graph:

            if vertex not in visited:

                component = []

                dfs(vertex, component)

                components.append(component)

        return components


# Create graph
g = Graph()

# Component 1
g.add_edge(0, 1)
g.add_edge(1, 2)

# Component 2
g.add_vertex(3)

# Component 3
g.add_edge(4, 5)
g.add_edge(5, 6)

# Find components
components = g.connected_components()

print("Connected Components:")

for i, component in enumerate(components, 1):

    print(
        "Component",
        i,
        ":",
        component
    )

print("Total Components:", len(components))