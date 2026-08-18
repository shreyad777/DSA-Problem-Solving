class DisjointSet:

    def __init__(self, n):

        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, vertex):

        if self.parent[vertex] != vertex:

            self.parent[vertex] = self.find(
                self.parent[vertex]
            )

        return self.parent[vertex]

    def union(self, vertex1, vertex2):

        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        # Same component → adding this edge
        # would create a cycle
        if root1 == root2:
            return False

        # Union by rank
        if self.rank[root1] < self.rank[root2]:

            self.parent[root1] = root2

        elif self.rank[root1] > self.rank[root2]:

            self.parent[root2] = root1

        else:

            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


def kruskal_mst(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])

    ds = DisjointSet(vertices)

    mst = []
    total_weight = 0

    for u, v, weight in edges:

        # Add edge only if it doesn't create a cycle
        if ds.union(u, v):

            mst.append((u, v, weight))
            total_weight += weight

            # MST contains V - 1 edges
            if len(mst) == vertices - 1:
                break

    return mst, total_weight


# Graph

vertices = 4

edges = [
    (0, 1, 2),
    (0, 2, 6),
    (1, 3, 3),
    (2, 3, 1)
]


mst, total_weight = kruskal_mst(
    vertices,
    edges
)


print("Kruskal's Minimum Spanning Tree:")

for u, v, weight in mst:

    print(
        u,
        "--",
        v,
        "weight =",
        weight
    )

print("Total Weight:", total_weight)