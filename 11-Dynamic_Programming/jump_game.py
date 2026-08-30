def can_jump(nums):

    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(
            farthest,
            i + nums[i]
        )
        if farthest >= len(nums) - 1:
            return True

    return True
nums = [2, 3, 1, 1, 4]
print("Can reach the last index:", can_jump(nums))