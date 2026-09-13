class Solution:
    def numDecodings(self, s):
        MOD = 10**9 + 7
        previous_two = 1
        previous_one = 0
        for i in range(len(s)):
            current = 0
            char = s[i]
            if char == "*":
                current += 9 * previous_two
            elif char != "0":
                current += previous_two
            if i > 0:
                previous = s[i - 1]
                if previous == "*" and char == "*":
                    current += 15 * previous_one
                elif previous == "*":
                    if char <= "6":
                        current += 2 * previous_one
                    else:
                        current += previous_one
                elif char == "*":
                    if previous == "1":
                        current += 9 * previous_one
                    elif previous == "2":
                        current += 6 * previous_one
                else:
                    number = int(previous + char)
                    if 10 <= number <= 26:
                        current += previous_one
            current %= MOD
            previous_two = previous_one
            previous_one = current
        return previous_one
s = input("Enter encoded message: ")
solution = Solution()
print("Number of Decodings:", solution.numDecodings(s))