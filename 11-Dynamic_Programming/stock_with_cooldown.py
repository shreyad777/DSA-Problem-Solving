def max_profit(prices):
    n = len(prices)
    if n <= 1:
        return 0
    hold = -prices[0]
    sold = 0
    rest = 0
    for i in range(1, n):
        previous_hold = hold
        previous_sold = sold
        previous_rest = rest
        hold = max(previous_hold, previous_rest - prices[i])
        sold = previous_hold + prices[i]
        rest = max(previous_rest, previous_sold)
    return max(sold, rest)
prices = list(map(int, input("Enter stock prices: ").split()))
print("Maximum Profit:", max_profit(prices))