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


# Search in BST
def search(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    if target < root.data:
        return search(root.left, target)

    return search(root.right, target)


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


# Search
target = 60

if search(root, target):
    print(target, "found in BST")
else:
    print(target, "not found in BST")