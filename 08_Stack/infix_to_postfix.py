# DSA - Stack Program 09: Infix to Postfix

def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    elif operator == "*" or operator == "/":
        return 2
    return 0


def infix_to_postfix(expression):
    stack = []
    result = ""

    for char in expression:

        # Operand
        if char.isalnum():
            result += char

        # Opening bracket
        elif char == "(":
            stack.append(char)

        # Closing bracket
        elif char == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()

        # Operator
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                result += stack.pop()

            stack.append(char)

    # Pop remaining operators
    while stack:
        result += stack.pop()

    return result


# Input expression
expression = "A+B*C"

result = infix_to_postfix(expression)

print("Infix Expression:", expression)
print("Postfix Expression:", result)