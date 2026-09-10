class Solution:
    def minimumTotal(self, triangle):
        dp = triangle[-1].copy()
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
solution = Solution()
print(solution.minimumTotal(triangle))