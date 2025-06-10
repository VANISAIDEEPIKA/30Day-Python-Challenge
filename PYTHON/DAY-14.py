def factorial(n):
    # Base case to avoid infinite recursion
    if n == 0 or n == 1:
        return 1
    # Recursive step: n * factorial(n - 1)
    return n * factorial(n - 1)

# Testing the factorial function
num = 5
print(f"Factorial of {num} is {factorial(num)}")