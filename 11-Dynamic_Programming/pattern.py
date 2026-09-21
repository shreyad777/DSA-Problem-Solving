class Solution:
    def find132pattern(self, nums):
        stack = []
        second = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])
        return False
nums = list(
    map(int, input("Enter elements: ").split())
)

solution = Solution()

print(
    "132 Pattern:",
    solution.find132pattern(nums)
)