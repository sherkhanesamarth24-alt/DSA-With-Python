# DSA - Queue Program 08: Reverse Queue Using Stack

from collections import deque

queue = deque([10, 20, 30, 40, 50])
stack = []

print("Original Queue:", list(queue))

# Step 1: Queue elements push into Stack
while queue:
    stack.append(queue.popleft())

# Step 2: Stack elements push back into Queue
while stack:
    queue.append(stack.pop())

print("Reversed Queue:", list(queue))