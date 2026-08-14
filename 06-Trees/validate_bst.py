class Node:

    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None


# Validate BST
def is_valid_bst(root, minimum, maximum):

    if root is None:
        return True

    if root.data <= minimum or root.data >= maximum:
        return False

    return (
        is_valid_bst(root.left, minimum, root.data)
        and
        is_valid_bst(root.right, root.data, maximum)
    )


# Create a valid BST
root = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)


# Validate
if is_valid_bst(root, float("-inf"), float("inf")):
    print("The tree is a valid BST")
else:
    print("The tree is not a valid BST")