class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def search_element(head, target):

    current = head
    position = 0

    while current is not None:

        if current.data == target:
            return position

        current = current.next
        position += 1

    return -1


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


# Search for an element
position = search_element(head, 30)


if position != -1:
    print("Element found at position", position)
else:
    print("Element not found")
    