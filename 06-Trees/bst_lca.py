# Question 69: Lowest Common Ancestor in a BST


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert into BST
def insert(root, value):

    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)

    elif value > root.data:
        root.right = insert(root.right, value)

    return root


# Find LCA
def find_lca(root, p, q):

    current = root

    while current is not None:

        if p < current.data and q < current.data:
            current = current.left

        elif p > current.data and q > current.data:
            current = current.right

        else:
            return current

    return None


# Create BST
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)


# Find LCA
p = 20
q = 40

lca = find_lca(root, p, q)

if lca:
    print("LCA of", p, "and", q, "is", lca.data)
else:
    print("LCA not found")
    