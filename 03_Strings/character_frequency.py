
# DSA - Strings Program 04: Character Frequency

def character_frequency(text):
    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


text = "programming"

result = character_frequency(text)

print("String:", text)
print("Character Frequency:")

for char, count in result.items():
    print(char, ":", count)
