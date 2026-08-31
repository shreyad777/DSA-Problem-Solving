class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
root = Node(10)

root.left = Node(5)
root.right = Node(20)

root.left.left = Node(3)
root.left.right = Node(7)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
print("Inorder traversal:")
inorder(root)
