def longest_common_subsequence(text1, text2):

    m = len(text1)
    n = len(text2)

    # DP table
    dp = [
        [0] * (n + 1)
        for _ in range(m + 1)
    ]

    # Fill the table
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:

                dp[i][j] = dp[i - 1][j - 1] + 1

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


text1 = "abcde"
text2 = "ace"

result = longest_common_subsequence(
    text1,
    text2
)

print("Length of LCS:", result)