def find_provinces(isConnected):

    n = len(isConnected)

    visited = set()

    provinces = 0

    def dfs(city):

        visited.add(city)

        for neighbor in range(n):

            if (
                isConnected[city][neighbor] == 1
                and neighbor not in visited
            ):
                dfs(neighbor)

    # Check every city
    for city in range(n):

        if city not in visited:

            provinces += 1

            dfs(city)

    return provinces


# Example

isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

result = find_provinces(isConnected)

print("Number of Provinces:", result)