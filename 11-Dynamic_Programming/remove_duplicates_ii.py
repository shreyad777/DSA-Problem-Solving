class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = []

        for char, count in stack:
            result.append(char * count)

        return "".join(result)


s = input("Enter string: ")
k = int(input("Enter k: "))

solution = Solution()

print(
    "Result:",
    solution.removeDuplicates(s, k)
)