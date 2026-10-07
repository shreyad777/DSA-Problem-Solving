class Solution:
    def minInsertions(self, s):
        insertions = 0
        needed = 0
        for char in s:
            if char == "(":
                needed += 2
            else:
                needed -= 1
                if needed < 0:
                    insertions += 1
                    needed = 1
        return insertions + needed
s = input("Enter parentheses string: ")
solution = Solution()

print(
    "Minimum Insertions:",
    solution.minInsertions(s)
)