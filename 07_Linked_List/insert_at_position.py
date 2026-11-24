# DSA - Linked List Program 04: Insert at Specific Position

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_position(head, data, position):
    new_node = Node(data)

    if position == 1:
        new_node.next = head
        return new_node

    current = head

    for i in range(position - 2):
        if current is None:
            print("Invalid position")
            return head

        current = current.next

    if current is None:
        print("Invalid position")
        return head

    new_node.next = current.next
    current.next = new_node

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

print("Before Insertion:")
traverse(head)

# Insert 25 at position 3
head = insert_at_position(head, 25, 3)

print("After Insertion:")
traverse(head)