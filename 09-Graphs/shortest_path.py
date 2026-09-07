from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
    def shortest_path(self, start, target):
        if start not in self.graph or target not in self.graph:
            return None
        queue = deque([start])
        visited = {start}
        distance = {start: 0}
        parent = {start: None}
        while queue:
            vertex = queue.popleft()
            if vertex == target:
                break
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distance[neighbor] = distance[vertex] + 1
                    parent[neighbor] = vertex
                    queue.append(neighbor)
        if target not in distance:
            return None
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return distance[target], path
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 4)
result = g.shortest_path(0, 4)
if result:
    distance, path = result
    print("Shortest distance:", distance)
    print("Shortest path:", path)
else:
    print("No path exists")