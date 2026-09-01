import heapq


def prim_mst(graph):

    # Start from vertex 0
    start = 0

    visited = set()

    # (weight, current_vertex, parent)
    min_heap = [(0, start, -1)]

    mst = []
    total_weight = 0

    while min_heap:

        weight, vertex, parent = heapq.heappop(min_heap)

        # Skip already visited vertices
        if vertex in visited:
            continue

        visited.add(vertex)

        # Add edge to MST
        if parent != -1:

            mst.append(
                (parent, vertex, weight)
            )

            total_weight += weight

        # Explore neighbors
        for neighbor, edge_weight in graph[vertex]:

            if neighbor not in visited:

                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbor, vertex)
                )

    return mst, total_weight


# Graph

graph = {
    0: [(1, 2), (2, 6)],
    1: [(0, 2), (3, 3)],
    2: [(0, 6), (3, 1)],
    3: [(1, 3), (2, 1)]
}


mst, total_weight = prim_mst(graph)


print("Minimum Spanning Tree:")

for parent, vertex, weight in mst:

    print(
        parent,
        "--",
        vertex,
        "weight =",
        weight
    )

print("Total Weight:", total_weight)
