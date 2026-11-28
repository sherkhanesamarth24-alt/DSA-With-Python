# DSA - Queue Program 04: Queue Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue")

    # Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return removed

    # Peek
    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    # Check empty
    def is_empty(self):
        return self.front is None

    # Display
    def display(self):
        current = self.front

        print("Queue:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


# Create Queue
q = Queue()

# Insert elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

# Remove element
print("Dequeued:", q.dequeue())

# Front element
print("Front Element:", q.peek())

# Final queue
q.display()