def edit_distance(word1, word2):

    m = len(word1)
    n = len(word2)

    # Create DP table
    dp = [
        [0] * (n + 1)
        for _ in range(m + 1)
    ]

    # Convert word1 to empty string
    for i in range(m + 1):
        dp[i][0] = i

    # Convert empty string to word2
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the table
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1]

            else:

                insert = dp[i][j - 1] + 1

                delete = dp[i - 1][j] + 1

                replace = dp[i - 1][j - 1] + 1

                dp[i][j] = min(
                    insert,
                    delete,
                    replace
                )

    return dp[m][n]


word1 = "horse"
word2 = "ros"

result = edit_distance(word1, word2)

print("Edit distance:", result)