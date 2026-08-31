from collections import deque
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

def level_order(root):

    if root is None:
        return

    queue = deque()

    queue.append(root)

    while queue:

        current = queue.popleft()

        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
print("Level order traversal:")
level_order(root)
