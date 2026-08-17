def flood_fill(image, start_row, start_col, new_color):

    rows = len(image)
    cols = len(image[0])

    original_color = image[start_row][start_col]

    # If colors are already the same
    if original_color == new_color:
        return image

    def dfs(row, col):

        # Check boundaries
        if row < 0 or row >= rows:
            return

        if col < 0 or col >= cols:
            return

        # Only replace original color
        if image[row][col] != original_color:
            return

        # Change color
        image[row][col] = new_color

        # Up
        dfs(row - 1, col)

        # Down
        dfs(row + 1, col)

        # Left
        dfs(row, col - 1)

        # Right
        dfs(row, col + 1)

    dfs(start_row, start_col)

    return image


# Example image

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

result = flood_fill(image, 1, 1, 2)

print("Flood Filled Image:")

for row in result:
    print(row)