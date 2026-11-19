# DSA - Searching Program 05: Last Occurrence

def last_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            left = mid + 1

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result


numbers = [10, 20, 20, 20, 30, 40, 50]
target = 20

result = last_occurrence(numbers, target)

if result != -1:
    print("Last Occurrence at Index:", result)
else:
    print("Element Not Found")