# DSA - Sorting Program 08: Sort Array by Parity

def sort_by_parity(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:

        # Even number already on left
        if numbers[left] % 2 == 0:
            left += 1

        # Odd number already on right
        elif numbers[right] % 2 != 0:
            right -= 1

        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

    return numbers


numbers = [3, 1, 2, 4, 7, 6, 8]

print("Original Array:", numbers)

result = sort_by_parity(numbers)

print("Sorted by Parity:", result)