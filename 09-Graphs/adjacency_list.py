class Graph:

    def __init__(self):
        self.graph = {}

    # Add a vertex
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an undirected edge
    def add_edge(self, vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Display graph
    def display(self):

        for vertex in self.graph:

            print(
                vertex,
                "->",
                self.graph[vertex]
            )


# Create graph
g = Graph()

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Display
g.display()