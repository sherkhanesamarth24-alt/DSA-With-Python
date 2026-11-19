
# DSA - Searching Program 01: Linear Search

def linear_search(numbers, target):

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print("Element Found at Index:", result)
else:
    print("Element Not Found")
