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


# Inorder: Left -> Root -> Right
def inorder(root):

    if root is None:
        return

    inorder(root.left)

    print(root.data, end=" ")

    inorder(root.right)


# Preorder: Root -> Left -> Right
def preorder(root):

    if root is None:
        return

    print(root.data, end=" ")

    preorder(root.left)

    preorder(root.right)


# Postorder: Left -> Right -> Root
def postorder(root):

    if root is None:
        return

    postorder(root.left)

    postorder(root.right)

    print(root.data, end=" ")


# Display traversals
print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)