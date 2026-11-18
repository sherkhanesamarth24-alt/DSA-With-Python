
# DSA - Strings Program 06: Remove Duplicate Characters

def remove_duplicates(text):
    result = ""

    for char in text:
        if char not in result:
            result += char

    return result


text = "programming"

result = remove_duplicates(text)

print("Original String:", text)
print("After Removing Duplicates:", result)
