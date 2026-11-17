
# DSA - Arrays Program 07: Find Missing Number

def find_missing_number(numbers, n):
    total = n * (n + 1) // 2
    array_sum = sum(numbers)

    missing = total - array_sum

    return missing


numbers = [1, 2, 4, 5, 6]
n = 6

result = find_missing_number(numbers, n)

print("Array:", numbers)
print("Missing Number:", result)
