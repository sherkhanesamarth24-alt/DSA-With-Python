# DSA - Sorting Program 07: Sort 0s, 1s and 2s

def sort_colors(numbers):
    low = 0
    mid = 0
    high = len(numbers) - 1

    while mid <= high:

        if numbers[mid] == 0:
            numbers[low], numbers[mid] = numbers[mid], numbers[low]
            low += 1
            mid += 1

        elif numbers[mid] == 1:
            mid += 1

        else:
            numbers[mid], numbers[high] = numbers[high], numbers[mid]
            high -= 1

    return numbers


numbers = [2, 0, 2, 1, 1, 0]

print("Original Array:", numbers)

result = sort_colors(numbers)

print("Sorted Array:", result)