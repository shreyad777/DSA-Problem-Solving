class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert into BST
def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


# Find height of BST
def height(root):

    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


# Find height
tree_height = height(root)

print("Height of BST:", tree_height)