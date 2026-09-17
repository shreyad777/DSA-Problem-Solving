class Solution:
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                previous_day = stack.pop()
                result[previous_day] = i - previous_day
            stack.append(i)
        return result
temperatures = list(
    map(int, input("Enter temperatures: ").split())
)
solution = Solution()
print(
    "Days to Wait:",
    solution.dailyTemperatures(temperatures)
)