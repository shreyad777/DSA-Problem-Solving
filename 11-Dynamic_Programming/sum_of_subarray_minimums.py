class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        result = 0
        for i in range(n + 1):
            current = arr[i] if i < n else float("-inf")

            while stack and arr[stack[-1]] > current:
                mid = stack.pop()

                left_boundary = stack[-1] if stack else -1

                left = mid - left_boundary
                right = i - mid

                result += (
                    arr[mid] * left * right
                )

            stack.append(i)

        return result % MOD


arr = list(
    map(int, input("Enter array elements: ").split())
)

solution = Solution()

print(
    "Sum of Subarray Minimums:",
    solution.sumSubarrayMins(arr)
)