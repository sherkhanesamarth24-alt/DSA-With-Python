# DSA - Linked List Program 06: Delete from End

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_from_end(head):
    if head is None:
        print("Linked List is empty")
        return None

    if head.next is None:
        return None

    current = head

    while current.next.next is not None:
        current = current.next

    current.next = None
    return head


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

print("Before Deletion:")
traverse(head)

# Delete last node
head = delete_from_end(head)

print("After Deletion:")
traverse(head)