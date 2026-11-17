
# DSA - Arrays Program 03: Second Largest Element

def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None

    return second_largest


numbers = [10, 50, 30, 80, 60, 80]

result = find_second_largest(numbers)

if result is not None:
    print("Second Largest Element:", result)
else:
    print("Second largest element does not exist")
