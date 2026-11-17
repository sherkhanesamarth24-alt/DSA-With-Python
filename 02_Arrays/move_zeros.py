
# DSA - Arrays Program 04: Move Zeros to End

def move_zeros(numbers):
    position = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[position] = numbers[i]
            position += 1

    while position < len(numbers):
        numbers[position] = 0
        position += 1

    return numbers


numbers = [0, 1, 0, 3, 12, 0, 5]

result = move_zeros(numbers)

print("Array after moving zeros:", result)
