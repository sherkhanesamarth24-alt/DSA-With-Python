# DSA - Recursion Program 06: Sum of Digits

def sum_of_digits(n):
    if n == 0:
        return 0

    return (n % 10) + sum_of_digits(n // 10)


number = 1234

result = sum_of_digits(number)

print("Number:", number)
print("Sum of Digits:", result)