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


# Find minimum node
def find_min(root):

    current = root

    while current.left is not None:
        current = current.left

    return current


# Delete a node
def delete(root, value):

    if root is None:
        return None

    if value < root.data:
        root.left = delete(root.left, value)

    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        # Case 1: No left child
        if root.left is None:
            return root.right

        # Case 2: No right child
        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = find_min(root.right)

        root.data = successor.data

        root.right = delete(root.right, successor.data)

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

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


print("Before deletion:")
inorder(root)

# Delete 30
root = delete(root, 30)

print("\nAfter deletion:")
inorder(root)