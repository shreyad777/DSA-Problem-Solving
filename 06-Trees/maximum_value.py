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

def find_max(root):

    if root is None:
        return float("-inf")

    left_max = find_max(root.left)
    right_max = find_max(root.right)

    return max(root.data, left_max, right_max)

maximum = find_max(root)

print("Maximum value:", maximum)
