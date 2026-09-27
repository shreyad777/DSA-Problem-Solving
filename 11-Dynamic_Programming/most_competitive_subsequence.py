class Solution:
    def mostCompetitive(self, nums, k):
        stack = []
        remove = len(nums) - k
        for num in nums:
            while (
                stack
                and remove > 0
                and stack[-1] > num
            ):
                stack.pop()
                remove -= 1
            stack.append(num)
        return stack[:k]
nums = list(
    map(int, input("Enter array elements: ").split())
)

k = int(input("Enter k: "))

solution = Solution()

print(
    "Most Competitive Subsequence:",
    solution.mostCompetitive(nums, k)
)