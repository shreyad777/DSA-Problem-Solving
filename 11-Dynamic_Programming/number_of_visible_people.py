class Solution:
    def canSeePersonsCount(self, heights):
        n = len(heights)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Shorter people are visible and can be removed
            while stack and heights[i] > stack[-1]:
                stack.pop()
                result[i] += 1

            # The first remaining taller person is also visible
            if stack:
                result[i] += 1

            stack.append(heights[i])

        return result


heights = list(
    map(int, input("Enter heights: ").split())
)

solution = Solution()

print(
    "Visible People:",
    solution.canSeePersonsCount(heights)
)