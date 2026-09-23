class Solution:
    def removeDuplicateLetters(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        stack = []
        used = set()
        for char in s:
            count[char] -= 1
            if char in used:
                continue
            while (
                stack
                and stack[-1] > char
                and count[stack[-1]] > 0
            ):
                removed = stack.pop()
                used.remove(removed)
            stack.append(char)
            used.add(char)
        return "".join(stack)


s = input("Enter string: ")

solution = Solution()

print(
    "Result:",
    solution.removeDuplicateLetters(s)
)