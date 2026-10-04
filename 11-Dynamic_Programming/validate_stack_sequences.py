class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        pop_index = 0
        for value in pushed:
            stack.append(value)
            while (
                stack
                and pop_index < len(popped)
                and stack[-1] == popped[pop_index]
            ):
                stack.pop()
                pop_index += 1
        return len(stack) == 0
pushed = list(
    map(int, input("Enter pushed sequence: ").split())
)
popped = list(
    map(int, input("Enter popped sequence: ").split())
)

solution = Solution()

print(
    "Valid Stack Sequence:",
    solution.validateStackSequences(pushed, popped)
)