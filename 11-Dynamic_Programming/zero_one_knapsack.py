def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [
        [0] * (capacity + 1)
        for _ in range(n + 1)
    ]
    for i in range(1, n + 1):
        for current_capacity in range(
            capacity + 1
        ):
            dp[i][current_capacity] = dp[
                i - 1
            ][current_capacity]
            if weights[i - 1] <= current_capacity:
                take = (
                    values[i - 1]
                    + dp[
                        i - 1
                    ][
                        current_capacity
                        - weights[i - 1]
                    ]
                )
                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    take
                )
    return dp[n][capacity]
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
result = knapsack(
    weights,
    values,
    capacity
)
print("Maximum value:", result)