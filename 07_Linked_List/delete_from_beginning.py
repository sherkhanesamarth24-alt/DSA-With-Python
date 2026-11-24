# DSA - Linked List Program 05: Delete from Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_from_beginning(head):
    if head is None:
        print("Linked List is empty")
        return None

    head = head.next
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

# Delete first node
head = delete_from_beginning(head)

print("After Deletion:")
traverse(head)