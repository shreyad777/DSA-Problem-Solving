def number_of_islands(grid):

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    islands = 0

    def dfs(row, col):

        # Check boundaries
        if row < 0 or row >= rows:
            return

        if col < 0 or col >= cols:
            return

        # Stop at water or visited land
        if grid[row][col] != "1":
            return

        # Mark as visited
        grid[row][col] = "0"

        # Up
        dfs(row - 1, col)

        # Down
        dfs(row + 1, col)

        # Left
        dfs(row, col - 1)

        # Right
        dfs(row, col + 1)

    for row in range(rows):

        for col in range(cols):

            if grid[row][col] == "1":

                islands += 1

                dfs(row, col)

    return islands


# Example grid

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "1", "0"],
    ["0", "0", "0", "1", "1"],
    ["0", "0", "0", "0", "0"],
    ["1", "0", "1", "1", "0"]
]


print("Number of Islands:", number_of_islands(grid))