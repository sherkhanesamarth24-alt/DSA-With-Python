# DSA - Recursion Program 08: Binary Search

def binary_search(numbers, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid

    elif numbers[mid] > target:
        return binary_search(numbers, target, left, mid - 1)

    else:
        return binary_search(numbers, target, mid + 1, right)


numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50

result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")