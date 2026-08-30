def max_subarray(nums):

    current_sum = nums[0]
    maximum_sum = nums[0]

    for i in range(1, len(nums)):

        current_sum = max(
            nums[i],
            current_sum + nums[i]
        )

        maximum_sum = max(
            maximum_sum,
            current_sum
        )

    return maximum_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print("Maximum subarray sum:", result)
