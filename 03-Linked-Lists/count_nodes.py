class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def count_nodes(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1
result = count_nodes(head)
print("Number of nodes:", result)