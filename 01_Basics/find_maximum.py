# DSA Program 02: Find Maximum Element

def find_maximum(numbers):

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


numbers = [25, 10, 45, 5, 80, 35]

result = find_maximum(numbers)

print("Array:", numbers)
print("Maximum Element:", result)