# DSA - Queue Program 03: Queue Using Deque

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue
    def enqueue(self, data):
        self.queue.append(data)
        print(data, "inserted into queue")

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.queue.popleft()

    # Peek
    def peek(self):
        if self.is_empty():
            return None

        return self.queue[0]

    # Check empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display
    def display(self):
        print("Queue:", list(self.queue))


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