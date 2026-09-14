class Solution:
    def maxSubarraySumCircular(self, nums):
        total = sum(nums)
        current_max = nums[0]
        maximum_sum = nums[0]
        current_min = nums[0]
        minimum_sum = nums[0]
        for i in range(1, len(nums)):
            current_max = max(
                nums[i],
                current_max + nums[i]
            )
            maximum_sum = max(
                maximum_sum,
                current_max
            )
            current_min = min(
                nums[i],
                current_min + nums[i]
            )
            minimum_sum = min(
                minimum_sum,
                current_min
            )
        if maximum_sum < 0:
            return maximum_sum
        circular_sum = total - minimum_sum
        return max(maximum_sum, circular_sum)
nums = list(map(int, input("Enter numbers: ").split()))
solution = Solution()
print("Maximum Circular Subarray Sum:",
      solution.maxSubarraySumCircular(nums))