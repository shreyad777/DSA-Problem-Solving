class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create root
root = Node(10)

# Add children
root.left = Node(5)
root.right = Node(20)

# Add children of 5
root.left.left = Node(3)
root.left.right = Node(7)


# Display tree values
print("Root:", root.data)
print("Left child:", root.left.data)
print("Right child:", root.right.data)
print("Left-left child:", root.left.left.data)
print("Left-right child:", root.left.right.data)
