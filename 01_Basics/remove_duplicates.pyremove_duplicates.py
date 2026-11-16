# DSA Program 08: Remove Duplicates from Array

def remove_duplicates(numbers):

    unique_numbers = []

    for num in numbers:

        if num not in unique_numbers:
            unique_numbers.append(num)

    return unique_numbers


numbers = [10, 20, 10, 30, 20, 40, 50, 30]

result = remove_duplicates(numbers)

print("Original Array:", numbers)
print("Array Without Duplicates:", result)