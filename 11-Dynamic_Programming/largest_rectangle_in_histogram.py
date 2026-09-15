class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(
                    max_area,
                    h * width
                )
            stack.append(i)
        return max_area
heights = list(
    map(int, input("Enter histogram heights: ").split())
)
solution = Solution()
print(
    "Largest Rectangle Area:",
    solution.largestRectangleArea(heights)
)