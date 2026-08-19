def coin_change(coins, amount):

    # Initialize DP array
    dp = [float("inf")] * (amount + 1)

    # Zero coins are needed for amount 0
    dp[0] = 0

    # Calculate minimum coins for every amount
    for current_amount in range(1, amount + 1):

        for coin in coins:

            if coin <= current_amount:

                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    # If amount cannot be formed
    if dp[amount] == float("inf"):
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

result = coin_change(coins, amount)

print("Minimum number of coins:", result)