def calculator():
    print("Simple Python Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                print(f"Result: {num1 + num2}")
            elif operator == '-':
                print(f"Result: {num1 - num2}")
            elif operator == '*':
                print(f"Result: {num1 * num2}")
            elif operator == '/':
                if num2 != 0:
                    print(f"Result: {num1 / num2}")
                else:
                    print("Error: Cannot divide by zero.")
            else:
                print("Invalid operator. Please use +, -, *, or /")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

calculator()