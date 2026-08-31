class Node:

    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root

def find_max(root):

    if root is None:
        return None

    current = root

    while current.right is not None:
        current = current.right

    return current.data

root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)
maximum = find_max(root)
print("Maximum value:", maximum)