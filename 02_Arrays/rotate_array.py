
# DSA - Arrays Program 05: Rotate Array by One Position

def rotate_array(numbers):
    if len(numbers) == 0:
        return numbers

    first = numbers[0]

    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i + 1]

    numbers[-1] = first

    return numbers


numbers = [10, 20, 30, 40, 50]

result = rotate_array(numbers)

print("Original Array: [10, 20, 30, 40, 50]")
print("Rotated Array:", result)
