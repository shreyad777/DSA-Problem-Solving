from collections import deque


def oranges_rotting(grid):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque()

    fresh_oranges = 0

    # Find all rotten and fresh oranges
    for row in range(rows):

        for col in range(cols):

            if grid[row][col] == 2:

                queue.append((row, col))

            elif grid[row][col] == 1:

                fresh_oranges += 1

    # Directions: up, down, left, right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    minutes = 0

    # BFS
    while queue and fresh_oranges > 0:

        # Process one complete level
        for _ in range(len(queue)):

            row, col = queue.popleft()

            for dr, dc in directions:

                new_row = row + dr
                new_col = col + dc

                # Check boundaries
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 1
                ):

                    # Make orange rotten
                    grid[new_row][new_col] = 2

                    fresh_oranges -= 1

                    queue.append((new_row, new_col))

        minutes += 1

    # If fresh oranges remain
    if fresh_oranges > 0:
        return -1

    return minutes


# Example

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

result = oranges_rotting(grid)

print("Minimum minutes:", result)