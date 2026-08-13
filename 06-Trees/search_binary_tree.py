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


# Search for a value
def search(root, target):

    if root is None:
        return False

    if root.data == target:
        return True

    return search(root.left, target) or search(root.right, target)


# Test
target = 7

if search(root, target):
    print(target, "found in the tree")
else:
    print(target, "not found in the tree")
    