# Problem 24: Insert a Node at a Specific Position
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_position(head, data, position):

    if position < 0:
        return head

    if position == 0:

        new_node = Node(data)

        new_node.next = head

        return new_node

    new_node = Node(data)

    current = head

    for i in range(position - 1):

        if current is None:
            return head

        current = current.next

    if current is None:
        return head

    new_node.next = current.next

    current.next = new_node

    return head


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1


# Insert 15 at position 2
head = insert_at_position(head, 15, 2)


# Traverse the linked list
current = head

while current is not None:

    print(current.data, end=" ")

    current = current.next