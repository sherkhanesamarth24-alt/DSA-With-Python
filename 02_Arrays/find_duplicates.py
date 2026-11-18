
# DSA - Arrays Program 08: Find Duplicate Elements

def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return sorted(duplicates)


numbers = [10, 20, 30, 20, 40, 10, 50, 30]

result = find_duplicates(numbers)

print("Original Array:", numbers)
print("Duplicate Elements:", result)
