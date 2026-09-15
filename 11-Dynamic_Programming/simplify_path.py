class Solution:
    def simplifyPath(self, path):
        stack = []
        parts = path.split("/")
        for part in parts:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)
path = input("Enter Unix path: ")
solution = Solution()
print("Simplified Path:", solution.simplifyPath(path))