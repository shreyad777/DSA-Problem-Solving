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


# Postorder traversal
def postorder(root):

    if root is None:
        return

    # Visit left subtree
    postorder(root.left)

    # Visit right subtree
    postorder(root.right)

    # Visit root
    print(root.data, end=" ")


# Display result
print("Postorder traversal:")
postorder(root)
