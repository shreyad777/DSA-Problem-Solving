class Solution:
    def minRemoveToMakeValid(self, s):
        chars = list(s)
        stack = []
        for i, char in enumerate(chars):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    chars[i] = ""

        # Remove unmatched '('
        while stack:
            index = stack.pop()
            chars[index] = ""

        return "".join(chars)


s = input("Enter string: ")

solution = Solution()

print(
    "Valid String:",
    solution.minRemoveToMakeValid(s)
)