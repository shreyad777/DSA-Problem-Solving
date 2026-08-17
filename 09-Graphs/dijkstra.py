import heapq


class Graph:

    def __init__(self):
        self.graph = {}

    # Add vertex
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add weighted undirected edge
    def add_edge(self, vertex1, vertex2, weight):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))

    # Dijkstra's algorithm
    def dijkstra(self, start):

        # Distance to every vertex
        distances = {
            vertex: float("inf")
            for vertex in self.graph
        }

        distances[start] = 0

        # Min heap
        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )

            # Ignore outdated heap entry
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_vertex]:

                new_distance = current_distance + weight

                # Found a shorter path
                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        return distances


# Create graph
g = Graph()

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)

# Run Dijkstra
distances = g.dijkstra(0)

print("Shortest distances from vertex 0:")

for vertex, distance in distances.items():

    print(
        vertex,
        "->",
        distance
    )