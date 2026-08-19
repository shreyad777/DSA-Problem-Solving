def unique_paths(m, n):

    # Create DP table
    dp = [
        [0] * n
        for _ in range(m)
    ]

    # First row
    for j in range(n):
        dp[0][j] = 1

    # First column
    for i in range(m):
        dp[i][0] = 1

    # Fill remaining cells
    for i in range(1, m):

        for j in range(1, n):

            dp[i][j] = (
                dp[i - 1][j]
                + dp[i][j - 1]
            )

    return dp[m - 1][n - 1]


m = 3
n = 3

print("Number of unique paths:", unique_paths(m, n))