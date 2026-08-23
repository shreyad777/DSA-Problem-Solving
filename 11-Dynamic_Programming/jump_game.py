# Question 130: Jump Game


def can_jump(nums):

    farthest = 0

    for i in range(len(nums)):

        # Current index cannot be reached
        if i > farthest:
            return False

        # Update the farthest reachable index
        farthest = max(
            farthest,
            i + nums[i]
        )

        # We can already reach the end
        if farthest >= len(nums) - 1:
            return True

    return True


nums = [2, 3, 1, 1, 4]

print("Can reach the last index:", can_jump(nums))