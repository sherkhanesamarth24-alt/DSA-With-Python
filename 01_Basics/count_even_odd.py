# DSA Program 06: Count Even and Odd Numbers

def count_even_odd(numbers):

    even_count = 0
    odd_count = 0

    for num in numbers:

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count


numbers = [10, 15, 20, 25, 30, 35, 40]

even, odd = count_even_odd(numbers)

print("Array:", numbers)
print("Even Numbers:", even)
print("Odd Numbers:", odd)