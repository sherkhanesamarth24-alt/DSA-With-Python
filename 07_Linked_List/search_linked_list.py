# DSA - Linked List Program 07: Search an Element

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search(head, target):
    current = head
    index = 0

    while current is not None:
        if current.data == target:
            return index

        current = current.next
        index += 1

    return -1


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

# Search element
target = 30
result = search(head, target)

print("Linked List:")
traverse(head)

if result != -1:
    print("Element", target, "found at index:", result)
else:
    print("Element", target, "not found")