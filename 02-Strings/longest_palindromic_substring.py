def longest_palindrome(s):

    n = len(s)

    if n <= 1:
        return s

    # DP table
    dp = [
        [False] * n
        for _ in range(n)
    ]

    start = 0
    max_length = 1

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    # Check substrings of increasing length
    for length in range(2, n + 1):

        for i in range(n - length + 1):

            j = i + length - 1

            if s[i] == s[j]:

                # Length 2
                if length == 2:
                    dp[i][j] = True

                # Length > 2
                elif dp[i + 1][j - 1]:
                    dp[i][j] = True

            if dp[i][j] and length > max_length:

                start = i
                max_length = length

    return s[start:start + max_length]


s = "babad"

result = longest_palindrome(s)

print("Longest palindromic substring:", result)