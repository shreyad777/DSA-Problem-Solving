def coin_change(coins, amount):

    # amount + 1 acts as infinity
    impossible = amount + 1

    dp = [impossible] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    for current_amount in range(1, amount + 1):

        for coin in coins:

            if coin <= current_amount:

                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )

    if dp[amount] == impossible:
        return -1

    return dp[amount]


coins = [1, 2, 5]
amount = 11

print(
    "Minimum coins:",
    coin_change(coins, amount)
)