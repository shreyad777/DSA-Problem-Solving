from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result
nums = list(map(int, input("Enter array: ").split()))
k = int(input("Enter window size k: "))
solution = Solution()
print("Sliding Window Maximum:",
      solution.maxSlidingWindow(nums, k))