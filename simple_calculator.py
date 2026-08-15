def calculator():
    """A simple command-line calculator."""
    print("--- Simple Calculator ---")
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Cannot divide by zero.")
                    continue
            else:
                print("Error: Invalid operation. Please use +, -, *, or /.")
                continue

            print(f"\n{num1} {operation} {num2} = {result}")
            break # Exit the loop after successful calculation

        except ValueError:
            print("Invalid input. Please enter valid numbers for both inputs.")

if __name__ == "__main__":
    calculator()