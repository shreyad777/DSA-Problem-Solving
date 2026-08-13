class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree
root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)


# Inorder traversal
def inorder(root):

    if root is None:
        return

    # Visit left subtree
    inorder(root.left)

    # Visit root
    print(root.data, end=" ")

    # Visit right subtree
    inorder(root.right)


# Display result
print("Inorder traversal:")
inorder(root)
