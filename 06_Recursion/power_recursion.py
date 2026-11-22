# DSA - Recursion Program 04: Power of a Number

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


base = 2
exponent = 5

result = power(base, exponent)

print(base, "raised to", exponent, "is:", result)