# DSA - Stack Program 05: Next Greater Element

def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


# Input array
arr = [4, 5, 2, 10, 8]

result = next_greater(arr)

print("Original Array:", arr)
print("Next Greater Elements:", result)