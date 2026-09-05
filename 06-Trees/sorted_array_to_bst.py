class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def sorted_array_to_bst(arr, left, right):
    if left > right:
        return None
    middle = (left + right) // 2
    root = Node(arr[middle])
    root.left = sorted_array_to_bst(
        arr,
        left,
        middle - 1
    )
    root.right = sorted_array_to_bst(
        arr,
        middle + 1,
        right
    )
    return root
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
arr = [10, 20, 30, 40, 50, 60, 70]
root = sorted_array_to_bst(
    arr,
    0,
    len(arr) - 1
)
print("Inorder traversal:")
inorder(root)