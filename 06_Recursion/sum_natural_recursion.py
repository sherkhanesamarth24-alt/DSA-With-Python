# DSA - Recursion Program 02: Sum of Natural Numbers

def sum_natural(n):
    if n == 0:
        return 0

    return n + sum_natural(n - 1)


number = 5

result = sum_natural(number)

print("Sum of Natural Numbers up to", number, "is:", result)