
# DSA - Arrays Program 02: Find All Occurrences

def find_occurrences(numbers, target):
    indexes = []

    for i in range(len(numbers)):
        if numbers[i] == target:
            indexes.append(i)

    return indexes


numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20

result = find_occurrences(numbers, target)

if result:
    print("Element found at indexes:", result)
    print("Total occurrences:", len(result))
else:
    print("Element not found")
