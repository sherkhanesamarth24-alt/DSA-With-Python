
# DSA - Strings Program 07: First Non-Repeating Character

def first_non_repeating(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    for char in text:
        if frequency[char] == 1:
            return char

    return None


text = "aabbcde"

result = first_non_repeating(text)

if result:
    print("First Non-Repeating Character:", result)
else:
    print("No Non-Repeating Character Found")
