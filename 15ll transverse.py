class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
node0 = Node(10)
node1 = Node(12)
node2 = Node(14)
node3 = Node(16)
node4 = Node(18)
node5 = Node(20)

# Connecting all nodes together
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

#printing the linked list
head = node0    # head is the first node of the linked list
current = head   # current is the pointer to the current node
while current is not None:
    print(current.data , end = "  -> ")
    current = current.next

