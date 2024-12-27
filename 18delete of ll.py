class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating nodes
head = Node(10)
node1 = Node(12)
node2 = Node(14)
node3 = Node(16)
node4 = Node(18)
node5 = Node(20)

# Connecting all nodes together
head.next = node1 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

"""
#deletion from begining 
if head is not None:
    head = head.next
"""

#deletations from end 
current = head
while current.next.next is not None:
    current = current.next
    current.next = None

"""
#deletation of particular node
current = head
while current.next.next.data != 18:
    current = current.next
current.next = current.next.next"""




#printing the linked list
current = head   # current is the pointer to the current node
while current is not None:
    print(current.data , end = "  -> ")
    current = current.next

 