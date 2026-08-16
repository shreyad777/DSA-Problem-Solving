class Graph:

    def __init__(self, vertices):

        self.vertices = vertices

        # Create V x V matrix
        self.matrix = [
            [0] * vertices
            for _ in range(vertices)
        ]

    # Add an undirected edge
    def add_edge(self, vertex1, vertex2):

        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1

    # Remove an edge
    def remove_edge(self, vertex1, vertex2):

        self.matrix[vertex1][vertex2] = 0
        self.matrix[vertex2][vertex1] = 0

    # Display matrix
    def display(self):

        for row in self.matrix:
            print(row)


# Create graph with 4 vertices
g = Graph(4)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

# Display
print("Adjacency Matrix:")
g.display()