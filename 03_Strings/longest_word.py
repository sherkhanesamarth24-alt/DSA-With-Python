
# DSA - Strings Program 09: Find Longest Word

def find_longest_word(sentence):
    words = sentence.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = "Python programming is very interesting"

result = find_longest_word(sentence)

print("Sentence:", sentence)
print("Longest Word:", result)
print("Word Length:", len(result))
