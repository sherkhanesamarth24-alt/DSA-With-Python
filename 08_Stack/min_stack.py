# DSA - Stack Program 07: Min Stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Push element
    def push(self, data):
        self.stack.append(data)

        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    # Pop element
    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return None

        removed = self.stack.pop()

        if removed == self.min_stack[-1]:
            self.min_stack.pop()

        return removed

    # Get minimum element
    def get_min(self):
        if not self.min_stack:
            return None

        return self.min_stack[-1]

    # Display
    def display(self):
        print("Stack:", self.stack)


# Create MinStack
s = MinStack()

s.push(30)
s.push(10)
s.push(20)
s.push(5)
s.push(15)

s.display()

print("Minimum Element:", s.get_min())

print("Popped:", s.pop())
print("Popped:", s.pop())

s.display()
print("Minimum Element:", s.get_min())