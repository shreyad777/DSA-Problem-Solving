class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                needed = min(dp[j], dp[j + 1]) - dungeon[i][j]
                dp[j] = max(1, needed)
        return dp[0]
dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]
solution = Solution()
print(solution.calculateMinimumHP(dungeon))