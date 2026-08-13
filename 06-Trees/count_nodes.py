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


# Count nodes
def count_nodes(root):

    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


# Display result
total = count_nodes(root)

print("Number of nodes:", total)
