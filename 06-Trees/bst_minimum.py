class Node:

    def _init_(self, data):
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


# Find minimum value
def find_min(root):

    if root is None:
        return None

    if root.left is None:
        return root.data

    return find_min(root.left)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


# Find minimum
minimum = find_min(root)

print("Minimum value:", minimum)