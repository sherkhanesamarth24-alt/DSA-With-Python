# DSA Program 07: Find Second Largest Element

def find_second_largest(numbers):

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:

        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest


numbers = [10, 25, 45, 30, 80, 60]

result = find_second_largest(numbers)

print("Array:", numbers)
print("Second Largest Element:", result)