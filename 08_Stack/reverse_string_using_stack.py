# DSA - Stack Program 04: Reverse String Using Stack

def reverse_string(text):
    stack = []

    # Push all characters
    for char in text:
        stack.append(char)

    reversed_string = ""

    # Pop characters in reverse order
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Input string
text = "PYTHON"

result = reverse_string(text)

print("Original String:", text)
print("Reversed String:", result)