class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        maximum_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                maximum_width = max(
                    maximum_width,
                    j - i
                )

        return maximum_width


nums = list(
    map(int, input("Enter array elements: ").split())
)

solution = Solution()

print(
    "Maximum Width Ramp:",
    solution.maxWidthRamp(nums)
)