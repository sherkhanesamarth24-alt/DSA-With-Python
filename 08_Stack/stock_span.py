# DSA - Stack Program 06: Stock Span Problem

def calculate_span(prices):
    n = len(prices)
    span = [0] * n
    stack = []

    for i in range(n):

        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span


# Stock prices
prices = [100, 80, 60, 70, 60, 75, 85]

result = calculate_span(prices)

print("Stock Prices:", prices)
print("Stock Span:", result)