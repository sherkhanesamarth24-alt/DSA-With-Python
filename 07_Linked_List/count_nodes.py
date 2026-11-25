# DSA - Linked List Program 08: Count Nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    current = head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count


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

print("Linked List:")
traverse(head)

total = count_nodes(head)
print("Total Nodes:", total)