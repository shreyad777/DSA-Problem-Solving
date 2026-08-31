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

def inorder_successor(root, target):

    successor = None
    current = root

    while current is not None:

        if target < current.data:
            successor = current
            current = current.left

        elif target > current.data:
            current = current.right

        else:
            # Target has a right subtree
            if current.right is not None:

                current = current.right

                while current.left is not None:
                    current = current.left

                successor = current

            break

    return successor

root = None
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

target = 50

successor = inorder_successor(root, target)

if successor:
    print("Inorder successor of", target, "is", successor.data)
else:
    print("No inorder successor exists")