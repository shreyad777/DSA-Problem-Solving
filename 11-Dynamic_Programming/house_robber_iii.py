class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)
            rob_current = node.val + left_skip + right_skip
            skip_current = max(left_rob, left_skip) + max(
                right_rob, right_skip
            )
            return (rob_current, skip_current)
        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)
root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
solution = Solution()
print(solution.rob(root))