# DSA - Stack Program 03: Balanced Parentheses

def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:

        # Opening brackets
        if char in "({[":
            stack.append(char)

        # Closing brackets
        elif char in ")}]":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[char]:
                return False

    return len(stack) == 0


# Test expressions
expressions = [
    "()[]{}",
    "({[]})",
    "([)]",
    "((("
]

for exp in expressions:
    if is_balanced(exp):
        print(exp, "-> Balanced")
    else:
        print(exp, "-> Not Balanced")