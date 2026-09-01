def max_product(nums):
    current_max = nums[0]
    current_min = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
       
        previous_max = current_max
        previous_min = current_min
        current_max = max(
            num,
            num * previous_max,
            num * previous_min
        )
        current_min = min(
            num,
            num * previous_max,
            num * previous_min
        )
        result = max(
            result,
            current_max
        )

    return result
nums = [2, 3, -2, 4]
print("Maximum product:", max_product(nums))
