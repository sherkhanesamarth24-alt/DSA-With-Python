
# DSA - Strings Program 03: Count Vowels and Consonants

def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if char.isalpha():
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


text = "Hello Python"

v, c = count_vowels_consonants(text)

print("String:", text)
print("Vowels:", v)
print("Consonants:", c)
