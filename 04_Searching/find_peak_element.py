# DSA - Searching Program 09: Find Peak Element

def find_peak_element(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        mid = (left + right) // 2

        if numbers[mid] < numbers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


numbers = [1, 3, 5, 4, 2]

result = find_peak_element(numbers)

print("Peak Element:", numbers[result])
print("Peak Index:", result)