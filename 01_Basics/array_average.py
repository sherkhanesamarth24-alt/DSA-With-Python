# DSA Program 09: Find Average of Array Elements

def calculate_average(numbers):

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return average


numbers = [10, 20, 30, 40, 50]

result = calculate_average(numbers)

print("Array:", numbers)
print("Average:", result)




## cd D:\DSA\DSA-With-Python