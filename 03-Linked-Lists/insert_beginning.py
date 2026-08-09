class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create the existing linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1


# Create a new node
new_node = Node(5)


# Insert the new node at the beginning
new_node.next = head
head = new_node


# Traverse the linked list
current = head

while current is not None:

    print(current.data, end=" ")

    current = current.next