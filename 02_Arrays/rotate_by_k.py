
# DSA - Arrays Program 06: Rotate Array by K Positions

def rotate_by_k(numbers, k):
    n = len(numbers)

    if n == 0:
        return numbers

    k = k % n

    rotated = numbers[k:] + numbers[:k]

    return rotated


numbers = [10, 20, 30, 40, 50]
k = 2

result = rotate_by_k(numbers, k)

print("Original Array:", numbers)
print("K:", k)
print("Rotated Array:", result)
