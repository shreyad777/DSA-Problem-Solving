def rob_linear(nums):

    previous_two = 0
    previous_one = 0

    for money in nums:

        current = max(
            previous_one,
            previous_two + money
        )

        previous_two = previous_one
        previous_one = current

    return previous_one


def rob(nums):

    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[0]


    case_one = rob_linear(nums[1:])
    case_two = rob_linear(nums[:-1])

    return max(case_one, case_two)
nums = [2, 3, 2]

print("Maximum money:", rob(nums))