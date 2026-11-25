# DSA - Stack Program 02: Stack Using Class

class Stack:
    def __init__(self):
        self.stack = []

    # Push element
    def push(self, data):
        self.stack.append(data)
        print(data, "pushed into stack")

    # Pop element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.stack.pop()

    # Peek top element
    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    # Check empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Create stack object
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)
s.push(40)

s.display()

# Pop element
print("Popped:", s.pop())

# Peek element
print("Top Element:", s.peek())

# Display after operations
s.display()