# DSA - Searching Program 06: Count Occurrences

def first_occurrence(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


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

first = first_occurrence(numbers, target)
last = last_occurrence(numbers, target)

if first == -1:
    print("Element Not Found")
else:
    count = last - first + 1
    print("Total Occurrences:", count)