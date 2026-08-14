class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Convert sorted array to balanced BST
def sorted_array_to_bst(arr, left, right):

    if left > right:
        return None

    # Find middle element
    middle = (left + right) // 2

    # Create root
    root = Node(arr[middle])

    # Create left subtree
    root.left = sorted_array_to_bst(
        arr,
        left,
        middle - 1
    )

    # Create right subtree
    root.right = sorted_array_to_bst(
        arr,
        middle + 1,
        right
    )

    return root


# Inorder traversal
def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Sorted array
arr = [10, 20, 30, 40, 50, 60, 70]


# Convert to BST
root = sorted_array_to_bst(
    arr,
    0,
    len(arr) - 1
)


# Display inorder traversal
print("Inorder traversal:")
inorder(root)