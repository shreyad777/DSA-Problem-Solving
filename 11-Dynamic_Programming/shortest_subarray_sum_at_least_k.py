from collections import deque
class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        queue = deque()
        result = n + 1
        for i in range(n + 1):
            while queue and prefix[i] - prefix[queue[0]] >= k:
                length = i - queue.popleft()
                result = min(result, length)
            while queue and prefix[queue[-1]] >= prefix[i]:
                queue.pop()
            queue.append(i)
        if result == n + 1:
            return -1
        return result


nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter target sum: "))

solution = Solution()

print("Shortest Subarray Length:", solution.shortestSubarray(nums, k))
