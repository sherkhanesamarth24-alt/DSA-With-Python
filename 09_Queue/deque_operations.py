# DSA - Queue Program 07: Deque Operations

from collections import deque

dq = deque()

# Insert at front
dq.appendleft(10)
dq.appendleft(20)

# Insert at rear
dq.append(30)
dq.append(40)

print("Deque:", dq)

# Delete from front
print("Deleted from Front:", dq.popleft())

# Delete from rear
print("Deleted from Rear:", dq.pop())

# Insert again
dq.appendleft(50)
dq.append(60)

# Final deque
print("Final Deque:", dq)