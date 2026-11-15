# DSA Program 03: Find Minimum Element

def find_minimum(numbers):

    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


numbers = [25, 10, 45, 5, 80, 35]

result = find_minimum(numbers)

print("Array:", numbers)
print("Minimum Element:", result)