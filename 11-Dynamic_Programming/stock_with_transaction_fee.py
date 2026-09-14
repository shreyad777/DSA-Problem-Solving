class Solution:
    def maxProfit(self, prices, fee):
        hold = float("-inf")
        cash = 0
        for price in prices:
            previous_hold = hold
            previous_cash = cash
            hold = max(
                previous_hold,
                previous_cash - price
            )
            cash = max(
                previous_cash,
                previous_hold + price - fee
            )
        return cash
prices = list(map(int, input("Enter stock prices: ").split()))
fee = int(input("Enter transaction fee: "))
solution = Solution()
print("Maximum Profit:", solution.maxProfit(prices, fee))