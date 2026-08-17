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

    # Find shortest path
    def shortest_path(self, start, target):

        if start not in self.graph or target not in self.graph:
            return None

        queue = deque([start])

        visited = {start}

        # Store distance from start
        distance = {start: 0}

        # Store parent for path reconstruction
        parent = {start: None}

        while queue:

            vertex = queue.popleft()

            # Target found
            if vertex == target:
                break

            for neighbor in self.graph[vertex]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    distance[neighbor] = distance[vertex] + 1

                    parent[neighbor] = vertex

                    queue.append(neighbor)

        # Target was not reached
        if target not in distance:
            return None

        # Reconstruct path
        path = []

        current = target

        while current is not None:

            path.append(current)

            current = parent[current]

        path.reverse()

        return distance[target], path


# Create graph
g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Find shortest path
result = g.shortest_path(0, 4)

if result:

    distance, path = result

    print("Shortest distance:", distance)
    print("Shortest path:", path)

else:

    print("No path exists")