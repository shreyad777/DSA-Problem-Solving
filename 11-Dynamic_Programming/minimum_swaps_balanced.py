class Solution:
    def minSwaps(self, s):
        balance = 0
        swaps = 0
        for char in s:
            if char == "[":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                swaps += 1
                balance = 1
        return swaps
s = input("Enter bracket string: ")
solution = Solution()
print(
    "Minimum Swaps:",
    solution.minSwaps(s)
)