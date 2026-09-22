class Solution:
    def largestPalindromic(self, num):
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1
        left = []
        for digit in range(9, -1, -1):
            pairs = count[digit] // 2
            if digit == 0 and not left:
                pairs = 0

            left.append(str(digit) * pairs)
            count[digit] -= pairs * 2

        left = "".join(left)

        # Find the largest remaining digit for the center
        middle = ""

        for digit in range(9, -1, -1):
            if count[digit] > 0:
                middle = str(digit)
                break

        # If everything was zero, return "0"
        if not left:
            return middle if middle else "0"

        return left + middle + left[::-1]


num = input("Enter digits: ")

solution = Solution()

print(
    "Largest Palindromic Number:",
    solution.largestPalindromic(num)
)