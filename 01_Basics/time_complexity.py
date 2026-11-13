# DSA - Time Complexity Examples

# O(1) - Constant Time
def get_first_element(arr):
    return arr[0]


# O(n) - Linear Time
def print_elements(arr):
    for element in arr:
        print(element)


# O(n^2) - Quadratic Time
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)


numbers = [10, 20, 30, 40, 50]

print("O(1) Example:")
print(get_first_element(numbers))

print("\nO(n) Example:")
print_elements(numbers)

print("\nO(n^2) Example:")
print_pairs(numbers)