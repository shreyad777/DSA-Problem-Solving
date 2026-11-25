from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        max_queue = deque()
        min_queue = deque()
        left = 0
        result = 0
        for right in range(len(nums)):
            while max_queue and nums[max_queue[-1]] < nums[right]:
                max_queue.pop()
            max_queue.append(right)
            while min_queue and nums[min_queue[-1]] > nums[right]:
                min_queue.pop()
            min_queue.append(right)
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                if max_queue[0] == left:
                    max_queue.popleft()                if min_queue[0] == left:
                    min_queue.popleft()
                left += 1

            result = max(result, right - left + 1)

        return result


nums = list(map(int, input("Enter array elements: ").split()))
limit = int(input("Enter limit: "))

solution = Solution()

print("Longest Valid Subarray:", solution.longestSubarray(nums, limit))