class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root):
        if root.left is None and root.right is None:
            return root.val == 1
        left_result = self.evaluateTree(root.left)
        right_result = self.evaluateTree(root.right)
        if root.val == 2:
            return left_result or right_result
        if root.val == 3:
            return left_result and right_result
root = TreeNode(
    2,
    TreeNode(1),
    TreeNode(
        3,
        TreeNode(0),
        TreeNode(1)
    )
)
solution = Solution()
print("Boolean Result:", solution.evaluateTree(root))