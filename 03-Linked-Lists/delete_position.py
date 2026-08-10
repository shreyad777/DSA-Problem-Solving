class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def delete_at_position(head, position):

    if head is None:
        return None

    if position < 0:
        return head

    if position == 0:
        return head.next

    current = head

    for i in range(position - 1):

        if current.next is None:
            return head

        current = current.next

    if current.next is None:
        return head

    current.next = current.next.next

    return head


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1


# Delete node at position 2
head = delete_at_position(head, 2)


# Traverse the linked list
current = head

while current is not None:

    print(current.data, end=" ")

    current = current.next