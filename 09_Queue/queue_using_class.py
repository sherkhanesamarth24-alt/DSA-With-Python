# DSA - Queue Program 02: Queue Using Class

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue element
    def enqueue(self, data):
        self.queue.append(data)
        print(data, "inserted into queue")

    # Dequeue element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        return self.queue.pop(0)

    # Peek front element
    def peek(self):
        if self.is_empty():
            return None

        return self.queue[0]

    # Check empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print("Queue:", self.queue)


# Create Queue object
q = Queue()

# Insert elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

# Remove element
print("Dequeued:", q.dequeue())

# Check front
print("Front Element:", q.peek())

# Display after operations
q.display()