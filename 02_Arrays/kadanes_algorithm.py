
# DSA - Arrays Program 11: Kadane's Algorithm

def max_subarray_sum(numbers):
    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for i in range(1, len(numbers)):
        current_sum = max(numbers[i], current_sum + numbers[i])
        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray_sum(numbers)

print("Array:", numbers)
print("Maximum Subarray Sum:", result)
