
# DSA - Strings Program 02: Palindrome Check

def is_palindrome(text):
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False


text = "MADAM"

if is_palindrome(text):
    print("Palindrome String")
else:
    print("Not a Palindrome String")
