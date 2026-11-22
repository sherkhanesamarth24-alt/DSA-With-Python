# DSA - Recursion Program 07: Palindrome

def is_palindrome(text, left, right):
    if left >= right:
        return True

    if text[left] != text[right]:
        return False

    return is_palindrome(text, left + 1, right - 1)


word = "madam"

result = is_palindrome(word, 0, len(word) - 1)

if result:
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")