def max_profit(k, prices):
    n = len(prices)
    if n == 0 or k == 0:
        return 0
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
    dp = [0] * (k + 1)
    for price in prices:
        for t in range(1, k + 1):
            dp[t] = max(
                dp[t],
                dp[t - 1] - price
            )
    buy = [float("-inf")] * (k + 1)
    sell = [0] * (k + 1)
    for price in prices:
        for t in range(1, k + 1):
            buy[t] = max(buy[t], sell[t - 1] - price)
            sell[t] = max(sell[t], buy[t] + price)
    return sell[k]
k = int(input("Enter maximum number of transactions: "))
prices = list(map(int, input("Enter stock prices: ").split()))
print("Maximum Profit:", max_profit(k, prices))