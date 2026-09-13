class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for current in range(coin, amount + 1):
                dp[current] += dp[current - coin]
        return dp[amount]
coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))
solution = Solution()
print("Number of Combinations:",
      solution.change(amount, coins))