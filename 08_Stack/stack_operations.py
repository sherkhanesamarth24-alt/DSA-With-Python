# DSA - Stack Program 01: Stack Operations

stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print("Stack:", stack)

# Pop operation
removed = stack.pop()
print("Popped Element:", removed)

print("Stack after Pop:", stack)

# Peek operation
print("Top Element:", stack[-1])

# Check if stack is empty
if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")