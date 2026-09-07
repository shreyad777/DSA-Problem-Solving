def flood_fill(image, start_row, start_col, new_color):
    rows = len(image)
    cols = len(image[0])
    original_color = image[start_row][start_col]
    if original_color == new_color:
        return image
    def dfs(row, col):
        if row < 0 or row >= rows:
            return
        if col < 0 or col >= cols:
            return
        if image[row][col] != original_color:
            return
        image[row][col] = new_color
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
    dfs(start_row, start_col)
    return image
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
result = flood_fill(image, 1, 1, 2)
print("Flood Filled Image:")
for row in result:
    print(row)