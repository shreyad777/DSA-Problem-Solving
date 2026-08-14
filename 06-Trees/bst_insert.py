class Node:

    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a value into BST
def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


# Inorder traversal
def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Create BST
root = None

root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)


# Display BST
print("BST in sorted order:")
inorder(root)