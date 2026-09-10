def is_interleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    m = len(s1)
    n = len(s2)
    dp = [
        [False] * (n + 1)
        for _ in range(m + 1)
    ]
    dp[0][0] = True
    for j in range(1, n + 1):
        dp[0][j] = (
            dp[0][j - 1]
            and s2[j - 1] == s3[j - 1]
        )
    for i in range(1, m + 1):
        dp[i][0] = (
            dp[i - 1][0]
            and s1[i - 1] == s3[i - 1]
        )
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            k = i + j - 1
            take_s1 = (
                dp[i - 1][j]
                and s1[i - 1] == s3[k]
            )
            take_s2 = (
                dp[i][j - 1]
                and s2[j - 1] == s3[k]
            )
            dp[i][j] = take_s1 or take_s2
    return dp[m][n]
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(
    "Can form s3 by interleaving:",
    is_interleave(s1, s2, s3)
)