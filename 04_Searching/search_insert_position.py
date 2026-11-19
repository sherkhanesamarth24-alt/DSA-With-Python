# DSA - Searching Program 07: Search Insert Position

def search_insert_position(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


numbers = [10, 20, 30, 40, 50]
target = 35

result = search_insert_position(numbers, target)

print("Insert Position:", result)