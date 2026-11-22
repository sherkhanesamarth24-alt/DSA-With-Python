# DSA - Recursion Program 05: Reverse a String

def reverse_string(text):
    if len(text) == 0:
        return text

    return reverse_string(text[1:]) + text[0]


word = "Python"

result = reverse_string(word)

print("Original String:", word)
print("Reversed String:", result)