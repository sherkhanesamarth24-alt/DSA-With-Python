# DSA - Searching Program 08: Search in Rotated Sorted Array

def search_rotated_array(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        # Check if left half is sorted
        if numbers[left] <= numbers[mid]:

            if numbers[left] <= target < numbers[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Otherwise, right half is sorted
        else:

            if numbers[mid] < target <= numbers[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


numbers = [40, 50, 60, 70, 10, 20, 30]
target = 20

result = search_rotated_array(numbers, target)

if result != -1:
    print("Element Found at Index:", result)
else:
    print("Element Not Found")