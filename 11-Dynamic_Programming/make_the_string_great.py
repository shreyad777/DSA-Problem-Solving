class Solution:
    def makeGood(self, s):
        stack = []
        for char in s:
            if (
                stack
                and stack[-1].lower() == char.lower()
                and stack[-1] != char
            ):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
s = input("Enter string: ")
solution = Solution()
print(
    "Result:",
    solution.makeGood(s)
)