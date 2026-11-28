# DSA - Queue Program 01: Queue Operations

queue = []

# Enqueue operation
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)

print("Queue:", queue)

# Dequeue operation
removed = queue.pop(0)
print("Dequeued Element:", removed)

print("Queue after Dequeue:", queue)

# Peek operation
print("Front Element:", queue[0])

# Check if queue is empty
if len(queue) == 0:
    print("Queue is Empty")
else:
    print("Queue is Not Empty")