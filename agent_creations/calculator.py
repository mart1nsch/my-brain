def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operation"

print("--- Simple Python Calculator ---")
try:
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    result = calculate(num1, num2, op)
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter numbers correctly.")