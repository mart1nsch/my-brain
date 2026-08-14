def fibonacci(n):
    """Returns the nth Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("Fibonacci sequence (first 10 numbers):")
    fib_gen = fibonacci(10)
    print(list(fib_gen))