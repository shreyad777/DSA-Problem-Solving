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


# Preorder traversal
def preorder(root):

    if root is None:
        return

    # Visit root
    print(root.data, end=" ")

    # Visit left subtree
    preorder(root.left)

    # Visit right subtree
    preorder(root.right)


# Display result
print("Preorder traversal:")
preorder(root)
