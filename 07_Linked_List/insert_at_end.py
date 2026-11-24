# DSA - Linked List Program 03: Insert at End

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


def traverse(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create initial linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before Insertion:")
traverse(head)

# Insert new node at end
head = insert_at_end(head, 40)

print("After Insertion:")
traverse(head)