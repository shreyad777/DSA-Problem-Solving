def find_length(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    dp = [0] * (n + 1)
    answer = 0
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if nums1[i - 1] == nums2[j - 1]:
                dp[j] = dp[j - 1] + 1
                answer = max(answer, dp[j])
            else:
                dp[j] = 0
    return answer
nums1 = list(map(int, input("Enter first array: ").split()))
nums2 = list(map(int, input("Enter second array: ").split()))
print("Maximum Length:", find_length(nums1, nums2))