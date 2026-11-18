
# DSA - Strings Program 01: Reverse a String

def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


text = "PYTHON"

result = reverse_string(text)

print("Original String:", text)
print("Reversed String:", result)
