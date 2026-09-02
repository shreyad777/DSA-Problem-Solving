class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def delete_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

head = delete_end(head)
current = head

while current is not None:
    print(current.data, end=" ")
    current = current.next
