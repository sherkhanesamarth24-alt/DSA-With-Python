# DSA - Queue Program 05: Circular Queue

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(data, "inserted")

    # Dequeue
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return None

        removed = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return removed

    # Peek
    def peek(self):
        if self.front == -1:
            return None
        return self.queue[self.front]

    # Display
    def display(self):
        print("Queue:", self.queue)


# Create Circular Queue
q = CircularQueue(5)

# Insert elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

# Remove elements
print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())

# Insert again (reuse empty spaces)
q.enqueue(50)
q.enqueue(60)

q.display()

# Front element
print("Front Element:", q.peek())