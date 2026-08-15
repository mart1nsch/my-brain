# Simple Python Calculator
def calculator():
    print("Select operation:")
    for num in ['add', 'subtract', 'multiply', 'divide']:
        print(f"1. {num}")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == 'add':
        try:
            n1, n2 = map(float, input("Enter first number: ").split())
            print(f"Result: {n1 + n2}")
        except ValueError:
            pass

    elif choice == 'subtract':
        try:
            n1, n2 = map(float, input("Enter first number and second number: ").split())
            print(f"Result: {n1 - n2}")
        except ValueError:
            pass

    elif choice == 'multiply':
        try:
            n1, n2 = map(float, input("Enter first number and second number: ").split())
            print(f"Result: {n1 * n2}")
        except ValueError:
            pass

    elif choice == 'divide':
        try:
            n1, n2 = map(float, input("Enter first number (dividend) and second number (divisor): ").split())
            if n2 != 0:
                print(f"Result: {n1 / n2}")
            else:
                print("Error: Cannot divide by zero.")
        except ValueError:
            pass

calculator()