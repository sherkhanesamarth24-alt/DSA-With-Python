# DSA - Linked List Program 01: Create and Traverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head points to first node
head = node1


# Traversal function
def traverse(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


print("Linked List:")
traverse(head)