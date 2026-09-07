import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))
    def dijkstra(self, start):
        distances = {
            vertex: float("inf")
            for vertex in self.graph
        }
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )
        return distances
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 5)
g.add_edge(2, 3, 1)
distances = g.dijkstra(0)
print("Shortest distances from vertex 0:")
for vertex, distance in distances.items():
    print(
        vertex,
        "->",
        distance
    )