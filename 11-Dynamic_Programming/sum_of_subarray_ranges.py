class Solution:
    def sumSubarrayMins(self, nums):
        n = len(nums)
        stack = []
        total = 0
        for i in range(n + 1):
            current = nums[i] if i < n else float("-inf")
            while stack and nums[stack[-1]] > current:
                mid = stack.pop()
                left = (
                    mid - stack[-1]
                    if stack
                    else mid + 1
                )
                right = i - mid

                total += nums[mid] * left * right

            stack.append(i)

        return total

    def sumSubarrayMaxs(self, nums):
        n = len(nums)
        stack = []
        total = 0

        for i in range(n + 1):
            current = nums[i] if i < n else float("inf")

            while stack and nums[stack[-1]] < current:
                mid = stack.pop()

                left = (
                    mid - stack[-1]
                    if stack
                    else mid + 1
                )

                right = i - mid

                total += nums[mid] * left * right

            stack.append(i)

        return total

    def subArrayRanges(self, nums):
        maximum_sum = self.sumSubarrayMaxs(nums)
        minimum_sum = self.sumSubarrayMins(nums)

        return maximum_sum - minimum_sum


nums = list(
    map(int, input("Enter array elements: ").split())
)

solution = Solution()

print(
    "Sum of Subarray Ranges:",
    solution.subArrayRanges(nums)
)