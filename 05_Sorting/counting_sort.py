# DSA - Sorting Program 06: Counting Sort

def counting_sort(numbers):
    if not numbers:
        return numbers

    max_value = max(numbers)
    min_value = min(numbers)

    count = [0] * (max_value - min_value + 1)

    for num in numbers:
        count[num - min_value] += 1

    sorted_array = []

    for i in range(len(count)):
        value = i + min_value

        for _ in range(count[i]):
            sorted_array.append(value)

    return sorted_array


numbers = [4, 2, 2, 8, 3, 3, 1]

print("Original Array:", numbers)

result = counting_sort(numbers)

print("Sorted Array:", result)