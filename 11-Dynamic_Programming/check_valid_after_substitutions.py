class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            stack.append(char)
            if len(stack) >= 3:
                if (
                    stack[-3] == "a"
                    and stack[-2] == "b"
                    and stack[-1] == "c"
                ):
                    stack.pop()
                    stack.pop()
                    stack.pop()

        return len(stack) == 0


s = input("Enter string: ")

solution = Solution()

print(
    "Valid String:",
    solution.isValid(s)
)