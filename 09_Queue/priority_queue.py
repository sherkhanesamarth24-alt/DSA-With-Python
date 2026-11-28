# DSA - Queue Program 06: Priority Queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Insert element with priority
    def enqueue(self, data, priority):
        self.queue.append((data, priority))
        print(data, "inserted with priority", priority)

    # Remove highest priority element
    def dequeue(self):
        if len(self.queue) == 0:
            print("Priority Queue is empty")
            return None

        highest = 0

        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[highest][1]:
                highest = i

        removed = self.queue.pop(highest)
        return removed[0]

    # Peek
    def peek(self):
        if len(self.queue) == 0:
            return None

        highest = 0

        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[highest][1]:
                highest = i

        return self.queue[highest][0]

    # Display
    def display(self):
        print("Priority Queue:", self.queue)


# Create Priority Queue
pq = PriorityQueue()

# Insert elements
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)
pq.enqueue("Task D", 1)

pq.display()

# Remove highest priority
print("Removed:", pq.dequeue())

# Peek
print("Highest Priority Element:", pq.peek())

# Final Queue
pq.display()