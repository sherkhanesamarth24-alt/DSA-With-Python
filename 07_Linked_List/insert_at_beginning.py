# DSA - Linked List Program 02: Insert at Beginning

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


def traverse(head):
    current = head

    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create initial linked list
head = Node(20)
head.next = Node(30)
head.next.next = Node(40)

print("Before Insertion:")
traverse(head)

# Insert new node
head = insert_at_beginning(head, 10)

print("After Insertion:")
traverse(head)