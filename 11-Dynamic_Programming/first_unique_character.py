from collections import deque
class Solution:
    def firstUniqChar(self, s):
        frequency = {}
        queue = deque()
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        for i, char in enumerate(s):
            if frequency[char] == 1:
                return i
        return -1


s = input("Enter a string: ")

solution = Solution()

result = solution.firstUniqChar(s)

print("First Unique Character Index:", result)