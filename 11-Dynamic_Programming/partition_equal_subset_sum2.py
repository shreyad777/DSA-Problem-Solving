def can_partition(nums):

    total = sum(nums)

    # Odd total cannot be divided equally
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[s] means:
    # Can we create sum s?
    dp = [False] * (target + 1)

    dp[0] = True

    for num in nums:

        # Go backwards because
        # each number can be used only once
        for current_sum in range(
            target,
            num - 1,
            -1
        ):

            dp[current_sum] = (
                dp[current_sum]
                or dp[current_sum - num]
            )

    return dp[target]


nums = [1, 5, 11, 5]

print(
    "Can partition equally:",
    can_partition(nums)
)