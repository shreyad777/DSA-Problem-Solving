def rob(nums):

    previous_two = 0
    previous_one = 0

    for money in nums:

        rob_current = money + previous_two

        skip_current = previous_one

        current = max(
            rob_current,
            skip_current
        )

        previous_two = previous_one
        previous_one = current

    return previous_one


nums = [2, 7, 9, 3, 1]

print("Maximum money:", rob(nums))