class Solution:
    def minAddToMakeValid(self, s):
        open_count = 0
        additions = 0
        for char in s:
            if char == "(":
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    additions += 1
        return additions + open_count
s = input("Enter parentheses string: ")
solution = Solution()
print(
    "Minimum Additions:",
    solution.minAddToMakeValid(s)
)
