class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [
            [0] * vertices
            for _ in range(vertices)
        ]
    def add_edge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 1
        self.matrix[vertex2][vertex1] = 1
    def remove_edge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 0
        self.matrix[vertex2][vertex1] = 0
    def display(self):
        for row in self.matrix:
            print(row)
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
print("Adjacency Matrix:")
g.display()