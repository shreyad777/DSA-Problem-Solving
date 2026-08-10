class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, data):

    new_node = Node(data)

    if head is None:
        return new_node

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node

    return head


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1


# Insert 40 at the end
head = insert_at_end(head, 40)


# Traverse the linked list
current = head

while current is not None:

    print(current.data, end=" ")

    current = current.next