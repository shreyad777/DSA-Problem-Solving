def jump(nums):

    n = len(nums)

    if n <= 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):

        # Farthest position reachable
        # from the current range
        farthest = max(
            farthest,
            i + nums[i]
        )

        # We have reached the end
        # of the current jump range
        if i == current_end:

            jumps += 1
            current_end = farthest

            # Already reached the end
            if current_end >= n - 1:
                break

    return jumps


nums = [2, 3, 1, 1, 4]

print("Minimum jumps:", jump(nums))