def fib(n):
    a, b = 0, 1  # First 2 Fibonacci numbers
    ctr = 2  # Counter for the numbers
    while ctr < n:
        a, b = b, a + b
        ctr += 1
    return b

def fib_test():
    # Base cases
    assert fib(0) == 0, "The 0th Fibonacci number should be 0"
    assert fib(1) == 1, "The 1st Fibonacci number should be 1"
    assert fib(2) == 1, "The 2nd Fibonacci number should be 1"
    assert fib(3) == 2, "The 3rd Fibonacci number should be 2"

    # Edge cases
    assert fib(-1) == 0, "Negative input should return 0"
    assert fib(100) == 354224848179261915075, "Large input should return correct value"

    # Other test cases
    assert fib(5) == 5, "The 5th Fibonacci number should be 5"
    assert fib(10) == 55, "The 10th Fibonacci number should be 55"
    assert fib(20) == 6765, "The 20th Fibonacci number should be 6765"

# Get user input for the n-th Fibonacci number
n = int(input("Enter the n-th Fibonacci number: "))

# Calculate and print the Fibonacci number
fib_num = fib(n)
print(f"The {n}-th Fibonacci number is: {fib_num}")