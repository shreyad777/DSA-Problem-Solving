class Solution:
    def maxProfit(self, prices):
        minimum_price = float("inf")
        maximum_profit = 0
        for price in prices:
            minimum_price = min(minimum_price, price)
            profit = price - minimum_price
            maximum_profit = max(maximum_profit, profit)
        return maximum_profit
prices = list(map(int, input("Enter stock prices: ").split()))
solution = Solution()
print("Maximum Profit:", solution.maxProfit(prices))