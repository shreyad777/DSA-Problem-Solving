class Node:
    def __init__(self, data):
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

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def delete(root, value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)
    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        successor = find_min(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)
    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

root = None
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    root = insert(root, value)
print("Before deletion:")
inorder(root)

root = delete(root, 30)

print("\nAfter deletion:")
inorder(root)