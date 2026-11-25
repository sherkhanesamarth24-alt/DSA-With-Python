# DSA - Linked List Program 09: Reverse Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def traverse(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original Linked List:")
traverse(head)

# Reverse the linked list
head = reverse_linked_list(head)

print("Reversed Linked List:")
traverse(head)