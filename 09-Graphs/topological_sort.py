from collections import deque


class Graph:

    def __init__(self):
        self.graph = {}

    # Add vertex
    def add_vertex(self, vertex):

        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add directed edge
    def add_edge(self, vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)

    # Topological Sort using Kahn's Algorithm
    def topological_sort(self):

        # Calculate indegree
        indegree = {
            vertex: 0
            for vertex in self.graph
        }

        for vertex in self.graph:

            for neighbor in self.graph[vertex]:

                indegree[neighbor] += 1

        # Queue vertices with indegree 0
        queue = deque()

        for vertex in indegree:

            if indegree[vertex] == 0:
                queue.append(vertex)

        result = []

        while queue:

            vertex = queue.popleft()

            result.append(vertex)

            # Remove outgoing edges
            for neighbor in self.graph[vertex]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycle
        if len(result) != len(self.graph):

            return None

        return result


# Create graph
g = Graph()

g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Perform topological sort
result = g.topological_sort()

if result:

    print("Topological Order:", result)

else:

    print("Topological sort is not possible.")
    print("Graph contains a cycle.")