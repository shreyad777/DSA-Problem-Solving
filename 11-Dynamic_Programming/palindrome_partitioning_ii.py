def min_cut(s):
    n = len(s)
    palindrome = [[False] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 1:
                palindrome[i][j] = True
            elif length == 2:
                palindrome[i][j] = (s[i] == s[j])
            else:
                palindrome[i][j] = (
                    s[i] == s[j]
                    and palindrome[i + 1][j - 1]
                )
    dp = [0] * n
    for i in range(n):
        if palindrome[0][i]:
            dp[i] = 0
        else:
            dp[i] = i
            for j in range(1, i + 1):
                if palindrome[j][i]:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[n - 1]
s = input("Enter a string: ")
print("Minimum cuts:", min_cut(s))