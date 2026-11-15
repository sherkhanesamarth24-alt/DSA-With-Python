# DSA Program 04: Reverse an Array

def reverse_array(numbers):

    left = 0
    right = len(numbers) - 1

    while left < right:

        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


numbers = [10, 20, 30, 40, 50]

print("Original Array:", numbers)

result = reverse_array(numbers)

print("Reversed Array:", result)