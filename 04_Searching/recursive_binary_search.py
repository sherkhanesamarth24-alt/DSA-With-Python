# DSA - Searching Program 03: Recursive Binary Search

def binary_search(numbers, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if numbers[mid] == target:
        return mid

    elif numbers[mid] < target:
        return binary_search(numbers, mid + 1, right, target)

    else:
        return binary_search(numbers, left, mid - 1, target)


numbers = [10, 20, 30, 40, 50, 60, 70]
target = 40

result = binary_search(numbers, 0, len(numbers) - 1, target)

if result != -1:
    print("Element Found at Index:", result)
else:
    print("Element Not Found")