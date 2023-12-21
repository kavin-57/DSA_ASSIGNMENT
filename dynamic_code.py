def fibonacci_dynamic_programming(n):
    fib = [0] * (n + 1)

    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Get user input for the position in the Fibonacci sequence
try:
    position = int(input("Enter the position in the Fibonacci sequence: "))
    if position < 0:
        raise ValueError("Position should be a non-negative integer.")
    
    result = fibonacci_dynamic_programming(position)
    print(f"The Fibonacci number at position {position} is: {result}")

except ValueError as e:
    print(f"Error: {e}. Please enter a valid non-negative integer.")
