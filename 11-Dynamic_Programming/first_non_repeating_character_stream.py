from collections import deque
class Solution:
    def FirstNonRepeating(self, stream):
        queue = deque()
        frequency = {}
        result = ""
        for char in stream:
            frequency[char] = frequency.get(char, 0) + 1
            queue.append(char)
            while queue and frequency[queue[0]] > 1:
                queue.popleft()
            if queue:
                result += queue[0]
            else:
                result += "#"
        return result
stream = input("Enter character stream: ")
solution = Solution()
print("Result:", solution.FirstNonRepeating(stream))