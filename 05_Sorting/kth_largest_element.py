# DSA - Sorting Program 09: Find Kth Largest Element

def kth_largest(numbers, k):
    sorted_numbers = sorted(numbers, reverse=True)

    return sorted_numbers[k - 1]


numbers = [7, 10, 4, 3, 20, 15]
k = 2

print("Original Array:", numbers)

result = kth_largest(numbers, k)

print("Kth Largest Element:", result)